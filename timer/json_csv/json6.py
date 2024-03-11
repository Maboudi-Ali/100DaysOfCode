import json
import csv

def json2csv(s_path, d_path):

    with open(s_path, 'r') as s_file:
        content = json.load(s_file)

    with open(d_path, 'w') as d_file:
        writer = csv.writer(d_file)
        for l in content:
            writer.writerow(l)

