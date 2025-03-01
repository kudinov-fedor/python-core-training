'''
for i in range(12):
    print(i)
    break
    print('Stop')


def simple_while_loop:
    x = 0
    while True:
        print(x)
        if >= limit:
            continue
        break
        x +=1


simple_while_loop()

some = None
x = 0
y = 5
try:
    some = x+y
except TypeError:
    print('TypeError happened')
'''

# Expressions
res = 'abbs'.replace('abb', 'pie')
print(res)

# Comparison Operations
if 1 <= 2 - 4:
    print('True')
else:
    print('False')

(False is True) == False # Check stackoverflow

False or 'some_val' and (not True and float())
# 1) Not
# 2) AND - takes 1st False object, or at least last one
# 3) OR/XOR - takes 2nd True object, or at least last one (False object)
# 4) ALL - goes item by item (if False, returns false and etc.)

def func(a = None):
    a = a or [1, 2, 3]
    print(a)
