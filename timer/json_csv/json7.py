import csv


def list2csv(lst, fname):
    with open(fname, 'w', newline='') as csvfile:
        fields = lst[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        for d in lst:
            writer.writerow(d)


data = [
    {'name': 'Alice', 'age': 25, 'height': 165, 'weight': 60},
    {'name': 'Bob', 'age': 30, 'height': 175, 'weight': 75}
]

list2csv(data, 'output.csv')

