import csv


def read_file(fname):
    with open(fname, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        for line in reader:
            yield dict(zip(header, line))


def calculate_sum(generator, colname):
    total = 0
    for d in generator:
        total += d.get(colname, 0)
    return total

