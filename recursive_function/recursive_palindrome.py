def is_palindrome(string, result=True):
    if len(string) > 1:
        if string[0] != string[-1]:
            result = False
        string = string[1:-1]
        return is_palindrome(string, result)
    else:
        return result


print(is_palindrome('alila'))

