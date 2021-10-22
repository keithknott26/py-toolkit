""" Demo loading and saving JSON"""
import json
from pprint import pprint

def serialize(filename, object_to_serialize):
    with open(filename, 'w+') as fout:
        json.dump(object_to_serialize, fout, indent=4)
        pprint(object_to_serialize)
        print('Saved to {}'.format(filename))

# Running the demo
print(">>> Deserialize JSON")
sample = {'name': 'Mark', 'age': 34, 'scores': [34.5, 45.1, 90.3]}
serialize('./samples/json/out1.json', sample)

sample = [{'code': 'A'}, {'code': 'B'}]
serialize('./samples/json/out2.json', sample)