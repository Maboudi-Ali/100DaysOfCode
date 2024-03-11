import json

def parser(json_string, key):
    file = json.loads(json_string)
    return file[key]

