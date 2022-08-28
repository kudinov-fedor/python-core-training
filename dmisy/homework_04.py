employees = [('Max', 'QA Engineer', 24),
             ('Anna', 'UI/UX Designer', 23),
             ('Amy', 'Computer Vision Engineer', 31),
             ('Bob', 'Full stack Developer', 29),
             ('William', 'Product Owner', 38)]
for employee in employees:
    print(employee[0], '-', employee[1])
    print('Age: ', employee[2])
age_younger = 'is the youngest employee in the team'
age_middle = 'is working here for quite some time'
age_older = 'is the oldest member of the team'
for age in employees:
    if age[2] < 25:
        print(age[0], 'who works as', age[1], age_younger)
    elif 25 <= age[2] <= 35:
        print(age[0], 'who works as', age[1], age_middle)
    elif age[2] >= 35:
        print(age[0], 'who works as', age[1], age_older)
    else:
        print('None of them works here')

print(hash(age_older))

try:
    print(5 / 0)
except ZeroDivisionError:
    print('This is error')


try:
    print(x)
except NameError:
    print('String is not defined')

try:
    print(y)
except ZeroDivisionError:
    print('String is not defined')
else:
    print('String is defined')
finally:
    print('Hey')