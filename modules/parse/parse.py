import pandas as pd
from typing import List, Dict
from definitions import PATH_USA_POP, DIR_DATA
import logging


def parse_states(
    value_field: str,
    selected_values: List[Dict],
    selected_fields: List[Dict],
    *,
    field_cleaners: Dict = None,
    file_partial: str = None,
) -> None:

    # read
    df = pd.read_csv(PATH_USA_POP, encoding="ISO-8859-1")

    # filter - remove statewide population counts
    df = df[df["COUNTY"] != 0]

    # filter - include only selected values
    selected_values_names = [x["name"] for x in selected_values]
    df = df[df[value_field].isin(selected_values_names)]

    # option - clean value field
    if field_cleaners:
        for field in field_cleaners.keys():
            cleaner_func = field_cleaners[field]
            df = cleaner_func(df, field)

    # rename field lookuptable
    rename_schema = {}
    for field in selected_fields:
        input_name = field["input_name"]
        output_name = field["output_name"]
        rename_schema[input_name] = output_name

    # group by
    by_state = df.groupby(value_field)

    for name, group in by_state:
        logging.info(f"Processing: {name}")
        # get selected state dict
        selected_state = list(filter(lambda x: x["name"] == name, selected_values))[0]

        # truncate
        selected_fields_input = [x["input_name"] for x in selected_fields]
        group = group[selected_fields_input]

        # rename
        group = group.rename(columns=rename_schema)

        # option - special processor (special funcs for doing extra stuff to df)
        special_processors = selected_state.get("special_processors")
        if special_processors:
            for processor in special_processors:
                group = processor(group)

        # produce csv
        abbrv = selected_state["abbrv"]
        filename = (
            f"{abbrv}-{file_partial}-pop.csv" if file_partial else f"{abbrv}-pop.csv"
        )
        output_path = DIR_DATA / filename
        group.to_csv(output_path, index=False)