def recursive_reverse(string):
    if string:
        last, string = string[-1], string[:-1]
        return last + recursive_reverse(string)
    else:
        return ''


print(recursive_reverse('ali'))
