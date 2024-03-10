s = open('sample.txt', 'r')
d = open('destination.txt', 'w')
d.write(s.read())
d.close()
s.close()

