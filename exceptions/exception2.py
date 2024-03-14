def read(path):
    try:
        with open(path, 'r') as f:
            print(f.read())

    except FileNotFoundError as e:
        print(e)

read('exception3.py')

