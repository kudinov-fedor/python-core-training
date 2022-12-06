import random

# print at stdout "Hello World:
print("Hello World")

"""
Multiline comment or doc-string
"""

name = "Luci"
print(name)

# Expressions using different operators
print("5 + 2 =", 5 + 2)
print("5 - 2 =", 5 - 2)
print("5 * 2 =", 5 * 2)
print("5 / 2 =", 5 / 2)
print("5 % 2 =", 5 % 2)
print("5 ** 2 =", 5 ** 2)
print("5 // 2 =", 5 // 2)

# Order of operations
print("1 + 2 - 3 * 2 =", 1 + 2 - 3 * 2)
print("(1 + 2 - 3) * 2 =", (1 + 2 - 3) * 2)

# work with strings
quote = "\"Always remember you are unique"
multi_line_quote = """ just 
like everyone else\""""
print(f"I like this quote {quote + multi_line_quote}", end=f"{'$' * 5}\n")

# practise with list
grocery_list = ["Juice", "Tomatoes", "Potatoes", "Bananas"]
print(f"Second item is {grocery_list[1]}")
grocery_list[1] = "Green Juice"
print(f"Second item is {grocery_list[1]}")

# slicing example
print(grocery_list[1:3])

# combine lists
other_events = ["Wash Car", "Pick Up Kids", "Cash Check"]
to_do_list = [other_events, grocery_list]
print(to_do_list[1][1])

grocery_list.append("Onion")
print(to_do_list)

grocery_list.insert(1, "Pickle")
grocery_list.remove("Bananas")
grocery_list.sort()
grocery_list.reverse()
del grocery_list[4]
print(to_do_list)

to_do_list2 = other_events + grocery_list
print("Length = ", len(to_do_list2))
print("Max value =", max(to_do_list2))
print("Min value =", min(to_do_list2))

# tuples
first_tuple = (1, 2, 3, 4, 5)
new_list = list(first_tuple)
new_tuple = tuple(new_list)
print("Length = ", len(new_tuple))
print("Max value =", max(new_list))
print("Min value =", min(new_tuple))

# dictionaries

super_villains = {
    "Fiddler": "Isaac Bowin",
    "Captain Cold": "Leonard Snart",
    "Weather Wizard": "Mark Mardon",
    "Mirror Master": "Sam Scudder",
    "Pied Piper": "Thomas Peterson"
}

print(super_villains["Captain Cold"])

del super_villains["Fiddler"]
super_villains["Pied Piper"] = "Hartley Rathaway"
print("Length=", len(super_villains))
print(super_villains.get("Pied Piper"))
print(super_villains.keys())
print(super_villains.values())

# Flow control
age = 29

if age >= 21:
    print("You should update you passport photo")
elif age >= 16:
    print("You must get you passport")
else:
    print("You are too young to have a passport, enjoy you life")

if 1 <= age <= 18:
    print("You get a birthday")
elif age == 21 or age >= 65:
    print("It's your best birthday")
elif age != 30:
    print("No birthday for you")
else:
    print("You get a cool birthday")

# loops

for i in range(1, 6):
    print(i, " ", end="")

print()

for product in grocery_list:
    print(product)

for x in [2, 4, 6, 8, 10]:
    print(x)

num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]

for group in num_list:
    for num in group:
        print(num, " ", end="")
print()

# random module
bottom = 0
top = 5
sentinel = 3


def function():
    return random.randrange(bottom, top)


print("With while loop")
random_num = random.randrange(bottom, top)

while random_num != sentinel:
    print(random_num)
    random_num = random.randrange(bottom, top)

print("With iter sentinel")
for number in iter(function, sentinel):
    print(number)

# string
long_string = "I'll catch you if you fall - The Floor"
print(long_string.capitalize())
print(long_string.find("Floor"))
print(long_string.isalnum())
print(long_string.isalpha())
print(len(long_string))
print(long_string.replace("Floor", "Ground"))
print(long_string.strip())
print(long_string.split(" "))
