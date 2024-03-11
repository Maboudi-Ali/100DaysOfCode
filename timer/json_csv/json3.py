import json

def parser(json_string, kw_pair):
    dictionary = json.loads(json_string)
    dictionary[kw_pair[0]] = kw_pair[1]

