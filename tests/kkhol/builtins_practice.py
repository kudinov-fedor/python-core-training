eq = 45 / 3 ** 4
eq2 = eq + 14
print(eq2)

name = 1.2 ** 2
print(name)

a = 2.2345
b = int(a)
print(b)

x = 1
y = 5
z = x + y
print(z)

# string

sent = 'we all like eating fruits'
sent1 = sent.capitalize()
print(sent1)

txt = 'I am {years} and I love {food} with {drink}'.format(years=30, food='fish', drink='milk')
print(txt)

r = '4560r836'
print(r.isdigit())

lotr = "In the first part of J.R.R. Tolkien's epic masterpiece, The Lord of the Rings, a shy young hobbit named Frodo Baggins " \
       "inherits a simple gold ring. He knows the ring has power, but not that he alone holds the secret to the survival--or " \
       "enslavement--of the entire world. Now Frodo, accompanied by a wizard, an elf, a dwarf, two men and three loyal hobbit " \
       "friends, must become the greatest hero the world has ever known to save the land and the people he loves."
lotr1 = lotr.find('save')
print(lotr1)


# list

ls = [5, 9.0, 12, 56]
del ls[:2]
print(ls[-1])
ls1 = [8, 0, 67]
g = ls is ls1
print(g)
ls.extend(ls1)
print(ls)
ls.reverse()
print(ls)

# dict

dict1 = {1: 'potato', 2: 56, 'c':'bananas'}
print(dict1[1])

dog = {'breed': 'chihuahua',
       'weight': 2.60,
       'origin': 'Mexico',
       'year': [1350, 1400, 1800]}
print(dog.get('weight'))
dog.update({'color': 'except merl'})
print(dog)

#set

animals = {'cat', 'dog', 'squirrel', 'munchkin'}
birds = {'parrot', 'chicken', 'rooster', 'dove'}
species = animals.union(birds)
print(species)
species1 = birds.issuperset(animals)
print(species1)
species2 = {'cat', 'dog', 'possum', 'squirrel', 'munchkin', 'hippo'}
species.intersection_update(species2)
print(species)