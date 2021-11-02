

benches = []


trees = []


people = []

dogs = []
animal = []

# print(dog.get_name())
# print(dog.DOG_POSITION)
# dog.bark()
# dog.move((1000, 2000))
# print(dog.get_position())
#
#
# # todo 1 problem new dog overrides prev dog
#
# print(dog.get_name())
# print(friend_dog.move((255, 561)))
#
# print(friend_dog.get_name())
# print(friend_dog.get_name())
# print(friend_dog.get_position())
#
#
# # todo problem 2 dog is all over the place
# for i in list(globals()):
#     print(i)
#
#
# import dog as street_dog
# import dog_2 as street_dog_2
# from fkudi import cat
#
# dogs.append(dog)
# dogs.append(friend_dog)
# dogs.append(street_dog)
# dogs.append(street_dog_2)
#
#
# for d in dogs:
#     print(d.BASE.get_name(d))
#     d.BASE.move(d, (100, 204))
#     print(d.BASE.get_position(d))
#     d.BASE.feed()
#
# print(cat.BASE.get_name(cat))
# print(cat.BASE.get_position(cat))
# cat.BASE.feed()


from pets_demo import base_dog, base_cat

new_cat_1 = base_cat.create(base_cat, name="NEW CAT", position=(0, 0))
new_cat_2 = base_cat.create(base_cat, position=(0, 0))
new_dog = base_dog.create(base_dog, position=(10, 10))


print(new_cat_1.BASE.get_name(new_cat_1))
new_cat_1.BASE.feed()
print(new_cat_2.BASE.get_name(new_cat_2))
new_cat_2.BASE.feed()
print(new_dog.BASE.get_name(new_dog))
new_dog.BASE.feed()

# todo we want to take automatically from base
#  we want when call automatically send self as 1 parameter
#  we want all basess in 1 module
