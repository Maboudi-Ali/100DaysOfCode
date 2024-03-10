with open('sample.txt', 'r') as f:
    doc = f.read()

search_word = input('word to search: ')
replace_word = input('word to replace: ')
updated_doc = doc.replace(search_word, replace_word)

with open('updated_document.txt', 'w') as g:
    g.write(updated_doc)

