def reverse(string):
    while string:
        yield string[-1]
        string = string[:-1]


for x in reverse('ali maboudi'): print(x)
