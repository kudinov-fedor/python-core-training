# Lecture 2
    # While Loop

str1 = 'Literature'
str2 = "Math"
while str1 == str2:
    print('This is Literature')
else:
    print('It is not Literature! It is a Math. Multiplication table for 3:')
i = 1
while i < 11:
    print(3*i)
    i = i+1


    # For Loop
print('Now, let`s do a countdown')
for i in range(11):
    print(i)
else:
    print('End of a countdown')
print('Let` try again and count to 30!')
for i2 in range(31):
    print(i2)
    if i2 >= 27:
        break
print('Something went wrong. Once more...')
for i3 in range(31):
    print(i3)
else:
    print('End of a countdown')
str = 'Moving forward'
if i3 == 30:
    print('Excellent!', str[0:6], str[7:14])


    # Functions
num = 350
def myFirstFunction():
    if num > 351:
        print('Print me')
    elif num == 352:
        print('Maybe me?')
    elif num != 350:
        print('Okay okay, move on')
    else:
        print('I see you are trying to master `Functions`? Good luck!')
myFirstFunction()

def myArgument(topic):
    if 5 == 3 + 2 * 2 / 2:
        print(topic)
myArgument('Here you go some facts below')

def fact1(rodent):
    print('Fact #1: ' + rodent + ' live only for 2-3 years')
fact1('Fancy rats')

def fact2(pet, pet2):
    print('Fact #2 ' + pet + ':')
    print(' - do like water')
    print(' - can swim')
    print(' - do not fight with ' + pet2)
fact2('Cats', 'dogs')

def factsRest(h1, h2, h3, h4):
    print('Fact #3 ' + h1 + ' is a 2nd ' + h2 + ' I am trying to learn after ' + h3)
    print('Fact #4 ' + h4 + ' is a planet')
    try:
        truth = h3 ** h4
        return truth
    except:
        print('I have handled this error btw')
factsRest('Python', 'programming language', 'JS', 'Moon')

    # Generators
def my_gen():
    n = True
    print('Fact #1')
    yield n
    n = True
    print('Fact #2')
    yield n
    n = 'I dropped learning JS'
    print('Fact #3')
    yield n
    n = False
    print('Fact #4')
    yield n
for new_yield in my_gen():
    print(new_yield)


    # Comperhensions
print('Moving to comprehensions. Here is the breakdown of the list:')
car_models = ['Volvo', 'Smart', 'Audi A8', 'Mini Cooper', 'BMW 7', 'Tesla', 'Tesla']
safety = []
for s in car_models:
    if 'l' in s:
        safety.append(s)
print(safety, ' - are safe cars to drive')

compact = []
for c in car_models:
    if 'r' in c:
        compact.append(c)
print(compact, ' - are compact cars, ideal for big cities')

luxury = []
for l in car_models:
    if '7' in l:
        luxury.append(l)
    elif '8' in l:
        luxury.append(l)
print(luxury, ' - are high class cars to show off on the streets')

    # Builtins
print('Playing a bit with built-ins')

car_models.sort()
print(car_models)

count = car_models.count('Tesla')
print(count)

index = car_models.index('Volvo')
print(index)

pop = car_models.pop(4)
print(pop)

muscle_cars = ['Pontiac', 'Buick', 'Dodge']
car_models.extend(muscle_cars)
print(car_models)


z = 1
while (z < 26):
    print('Information is processing...')
    z = z + 1
    if (z <= 13 and z >= 13):
        print('Error Found!')
    if (z == 13):
        print('Working on fixing the issue...')
    if (z == 13):
        print('Please wait...')
    if (z == 13):
        print('Issue is fixed. Moving forward.')
    elif (z <= 25):
        print('Loop', z, 'is done. Moving Forward.')
    elif (z >= 26):
        print('Loop', z, 'is done')
        print('Finished')