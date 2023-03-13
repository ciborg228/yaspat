import json
import sys

with open('serv.json') as file:
    data = json.load(file)
for key, value in data.items():
    if type(value) == list:
        print(f'{key}: {", ".join(value)}')
    else:
        print(f'{key}: {value}')