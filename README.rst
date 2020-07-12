# get-pop

A command line utility that generates CSVs of county-level population data for specified US states.

Data is based on 2019 U.S. census data.

The full documentation is hosted at [Read the Docs](https://get-pop.readthedocs.io/en/latest/index.html).

## Install

```pip install get-pop```

## Basic usage - command line

Type 'getpop' followed by the two letter postal code for one or more states. CSVs will be output
 in a new directory called 'data' in the current working directory.
 
Example #1: 
```
getpop ny

>> Initializing getpop
>> Selected states: ['ny']
>> Processing: New York
>> getpop complete
```
 
Example #2: 
  
```
getpop ny nj tx

>> Initializing getpop
>> Selected states: ['ny', 'nj', 'tx']
>> Processing: New Jersey
>> Processing: New York
>> Processing: Texas
>> getpop complete
```
Example #2: 

To get CSVs for all states, use:

  
## Basic usage - python
  
If you prefer, you can also import and call get-pop from within python:
  
```
from get_pop.get_pop import get_pop

states = ["ny","nj","tx","pa"]
get_pop(states)
```
## License
[MIT](https://choosealicense.com/licenses/mit/)