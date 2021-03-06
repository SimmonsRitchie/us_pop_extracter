from get_pop.modules.parse.helpers import clean_county, merge_nyc_boroughs

value_field = "STNAME"
field_cleaners = {"CTYNAME": clean_county}
state_index = [
    {"name": "Alabama", "abbrv": "al"},
    {"name": "Alaska", "abbrv": "ak"},
    {"name": "Arizona", "abbrv": "az"},
    {"name": "Arkansas", "abbrv": "ar"},
    {"name": "California", "abbrv": "ca"},
    {"name": "Colorado", "abbrv": "co"},
    {"name": "Connecticut", "abbrv": "ct"},
    {"name": "Delaware", "abbrv": "de"},
    {"name": "Florida", "abbrv": "fl"},
    {"name": "Georgia", "abbrv": "ga"},
    {"name": "Hawaii", "abbrv": "hi"},
    {"name": "Idaho", "abbrv": "id"},
    {"name": "Indiana", "abbrv": "in"},
    {"name": "Iowa", "abbrv": "ia"},
    {"name": "Kansas", "abbrv": "ks"},
    {"name": "Kentucky", "abbrv": "ky"},
    {"name": "Louisiana", "abbrv": "la"},
    {"name": "Maine", "abbrv": "me"},
    {"name": "Maryland", "abbrv": "md"},
    {"name": "Massachusetts", "abbrv": "ma"},
    {"name": "Michigan", "abbrv": "mi"},
    {"name": "Minnesota", "abbrv": "mn"},
    {"name": "Mississippi", "abbrv": "ms"},
    {"name": "Missouri", "abbrv": "mo"},
    {"name": "Montana", "abbrv": "mt"},
    {"name": "Nebraska", "abbrv": "ne"},
    {"name": "Nevada", "abbrv": "nv"},
    {"name": "New Hampshire", "abbrv": "nh"},
    {"name": "New Jersey", "abbrv": "nj"},
    {"name": "New Mexico", "abbrv": "nm"},
    {"name": "New York", "abbrv": "ny", "special_processors": [merge_nyc_boroughs]},
    {"name": "New Jersey", "abbrv": "nj"},
    {"name": "North Carolina", "abbrv": "nc"},
    {"name": "North Dakota", "abbrv": "nd"},
    {"name": "Ohio", "abbrv": "oh"},
    {"name": "Oklahoma", "abbrv": "ok"},
    {"name": "Oregon", "abbrv": "or"},
    {"name": "Pennsylvania", "abbrv": "pa"},
    {"name": "Rhode Island", "abbrv": "ri"},
    {"name": "South Carolina", "abbrv": "sc"},
    {"name": "South Dakota", "abbrv": "sd"},
    {"name": "Tennessee", "abbrv": "tn"},
    {"name": "Texas", "abbrv": "tx"},
    {"name": "Utah", "abbrv": "ut"},
    {"name": "Vermont", "abbrv": "vt"},
    {"name": "Virginia", "abbrv": "va"},
    {"name": "Washington", "abbrv": "wa"},
    {"name": "West Virginia", "abbrv": "wv"},
    {"name": "Wisconsin", "abbrv": "wi"},
    {"name": "Wyoming", "abbrv": "wy"},
]

default_fields = [
    {"input_name": "FIPS", "output_name": "fips"},
    {"input_name": "CTYNAME", "output_name": "name"},
    {"input_name": "POPESTIMATE2019", "output_name": "population"},
]
