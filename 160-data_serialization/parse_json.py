#!/usr/bin/env python3
import json

"""
json.load(f) # load data from a file
json.loads(s) # loads data from a string
json.dump(j,f) # dumps data to a file
json.dumps(j) # dumps data to a string
there could be no comments in a json file
"""

my_data =  '''{
    "name": true,
     "age": null,
     "items": [1,2,3,4],
     "more_dicts": [{
        "name": 10
     }, {
        "some_more": "€10"
     }
     ]
}'''

def write_json(j,file_path):
    with open(file_path,'w') as fd:
        json.dump(j, fd, indent=4, ensure_ascii = False)
def load_json(file_path):
    """
    Loads JSON from a file
    """
    with open(file_path,'r') as fd:
        data = json.load(fd)
        return data

def dumps_json(j):
    return json.dumps(j, sort_keys = False, indent = 4, ensure_ascii = False)

if __name__ == "__main__":
    print(load_json('./sample_json.json'))
    x = load_json('./sample_json.json')
    print(dumps_json(x))
    stream_lined  = json.loads(my_data)
    write_json(stream_lined, 'no_json.json')
