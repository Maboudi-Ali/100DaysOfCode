import json
from collections import Counter

def unique_counter(json_string):
    file = json.loads(json_string)
    values = list()
    for d in file:
        values.extend(d.values())
    return dict(Counter(values))

string = '[{"color": "red"}, {"color": "blue"}, {"color": "red"}, {"color": "green"}]'

print(unique_counter(string))

