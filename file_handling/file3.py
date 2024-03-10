from collections import Counter
from faker import Faker
from string import punctuation

faker = Faker()
with open('sample.txt', 'a') as f:
    f.write(faker.text())


translator = str.maketrans(punctuation, ' ' * len(punctuation))
with open('sample.txt', 'r') as g:
    res = dict()
    for line in g.readlines():
        line = line.translate(translator)
        res.update(dict(Counter(line.split())))

    for word, count in res.items():
        print(f'{word}: {count}')

