# Task_01
# User searching for city locations available in system
import sys


def func1():
    print("Task_01")
    cities = ['Sofia', 'Burgas', 'Plovdiv', 'Varna', 'Veliko Tarnovo', 'Ruse', 'Pleven']
    do = input('Welcome. Please enter a city to check available locations:\n')

    if do in cities:
        print(f'The city {do} is present as an active location.')
    else:
        print(f'Sorry. {do} is not present as an active location.')
    print()


# Task_02
# Generator function w/ yield that adds 10
def func2():
    print("Task_02")

    def generator01() -> object:
        numb = 1
        print('The current number is:')
        # Yield statement; shows current number
        yield numb

        numb += 10
        print('This is the result + 10:')
        yield numb

        numb += 10
        print('Adding another 10 and this is the final result')
        yield numb

    for item in generator01():
        print(item)
    print()


# Task_03
# Choose flight locations and check their schedules
def func3():
    print("Task_03")
    locations = {"Boston": "14:30", "Berlin": "10:00", "Barcelona": "04:00", "Cologne": "13:15"}
    sel = input("Hi. Please enter flight location: \n")
    if sel in locations:
        result = locations.get(sel)
        print("Flight to", sel, "is at:", result)
    else:
        print(f'Sorry. {sel} is not present as an active location.')
    print()


def mainf():
    a = '1'
    b = '2'
    c = '3'
    desc = input("Choose homework task between 1,2,3: \n")
    if desc == a:
        func1()
        mainf()
    elif desc == b:
        func2()
        mainf()
    elif desc == c:
        func3()
        mainf()
    elif desc == "exit":
        sys.exit()

mainf()
