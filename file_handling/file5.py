while (line := input()) != '':
    with open('notes.txt', 'a') as f:
        f.write(line + '\n')

