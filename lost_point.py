from collections import Counter
X = list()
Y = list()
Z = list()
for i in range(7):
	x, y, z = map(int, input().split())
	X.append(x)
	Y.append(y)
	Z.append(z)
x_res = Counter(X).most_common()[-1][0]
y_res = Counter(Y).most_common()[-1][0]
z_res = Counter(Z).most_common()[-1][0]
print(x_res, y_res, z_res)
