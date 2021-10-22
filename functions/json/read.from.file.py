""" Demo loading and saving JSON"""
import json
from pprint import pprint


def deserialize(filename):
    with open(filename, 'r') as f:
        # you can build the json directly from the file reader
        json_data = json.load(f)
        # Depending on the JSON format you get a different JSON object
        if isinstance(json_data, dict):
            print('json passed is an array --> python object is a dict')
            print('keys() = {}'.format(json_data.keys()))
        elif isinstance(json_data, list):
            print('json passed is an array --> python object is a list')
            print('len() = {}'.format(len(json_data)))
        else:
            print(type(json_data))
        return json_data
        
print(">>> Serialize JSON")
deserialize('./samples/json/in1.json')