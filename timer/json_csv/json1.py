import json

with open('dictionary.json', 'r') as f:
    dictionary = json.loads(f.read())

dictionary['foo'] = 4
print(dictionary)

