# Builtin expressions

cities = ('Rotterdam', 'Copenhagen', 'Kyiv', 'Ghent', 'Manchester', 'Dublin', 'New York')
order = enumerate(cities)
print(tuple(order))

capital1 = list('Istanbul')
capital1 = []
capital2 = list('Bucharest')
w_capital = []

for c_c in 'Istanbul':
    capital1.append(c_c)
for w_c in 'Bucharest':
    capital2.append(w_c)
print(capital1, ' and', capital2)

b = bytearray(7)
print(b)

f = bool(0 * 50)
e = int(-5.6 * 12)
print(e)
if f <= e:
    print('True')
else:
    print(f)  # Bool returns 'False' if the object is false


def myCities(c):
    return len(c)
d = map(myCities, cities)
print(list(d))

x1 = 64
x2 = 8 ** 2
if x1 is x2:
    print(x1 == x2)


