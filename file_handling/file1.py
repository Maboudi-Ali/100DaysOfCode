while (word := input()) != 'exit':
    with open('output.txt', 'a') as f:
        f.write(word + '\n')

