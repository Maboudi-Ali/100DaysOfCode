def get(dictionary, key):
    try:
        value = dictionary[key]
        print(value)
    except KeyError:
        print('Key not Found')


d = {'name': 'Ali',}
get(d, 'name')
get(d, 'age')

