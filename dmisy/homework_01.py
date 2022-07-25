# General Practice
# Strings
s = 'I love Python 3.9'
s1 = s.count('v')
s2 = s.isnumeric()
s3 = s.upper()
s4 = s.swapcase()

print(len(s))
print(s[:6])
print(s[7:18],'!')
print('Java' in s)
print('like' not in s)
print('There are', s1, 'v letter in here')
print(s2,', it is not numeric')
print(s3)
print(s4)

# Operators
a = 50
if a >= 100:
    print('Correct')
elif a == 500 / 50:
    print('Number equals 100')
elif a < 21.50 + 20.60:
    print('Number is lower than 50')
else:
    print('Incorrect')

# List/Array/Tuple/Set
breakfast_list = ['milk, coffee, tea, sugar, bread, cheese, ham, berries']
dinner_list = ['soup', 'chicken breasts', 'couscous', 'sweet potato']
points = [1, 2, 3, 5, 8, 13, 21, 34, 5, 50, 13]
set1 = {'rat', 'mouse', 'squirrel'}
set2 = {'mouse', 'cat', 'penguin'}

breakfast_list.append('cream')
breakfast_list.insert(8,'juice')
breakfast_list.sort()
print(breakfast_list)

points.reverse()
points.remove(5)
points.remove(13)
count = points.count(13)
index = points.index(21)
print(points)
print(count)
print(index)

dinner_list.pop(2)
print(dinner_list, 'nothing to eat for a dinner :(')

similar = set1.intersection(set2)
set2.discard('penguin')
print(similar)
print(set2)

# Dictionaries
company = {
    'accounting': '7 employees',
    'sales': '15 employees',
    'HR': '4 employees'
}

key = company.keys()
employees = company.pop('sales')
numbers = company.values()
print(key)
print(employees)
print(numbers) # Why it ignores 15?