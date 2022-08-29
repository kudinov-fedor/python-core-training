import random
import  sys
import os
#
# # print("Hello world")
# #
# # name = "Viktor"
# # print(name)
# # print('1 - 2 + 4 =', 6 - 1)
# #
# # quote = "\"Always remember you are unique!!!"
# #
# # multi_line_quote = '''
# # just like
# # everyone
# # else
# # '''
# # new_string = quote + multi_line_quote
# # #print(new_string)
# # print("%s %s %s" % ('I like qoutes', quote, multi_line_quote))
# # print('\n' * 1)
# # print("I don't like ", end="")
# # print("newlines")
# #
# grocery_list = ['juice', 'Tomatoes', 'Potatoes', 'Bananas']
# # print('First item', grocery_list[0])
#
# grocery_list[0] = 'Green Juice'
# # print(grocery_list[0])
# # print(grocery_list[1:3])    # как отобразить ['Tomatoes', 'Potatoes'] - без квадратных скобок?
#
# other_events = ['Car wash', 'Pick up kids', 'Cash check']
# to_do_list = [other_events, grocery_list]
# # print(to_do_list)
# print((to_do_list[1][1]))
# grocery_list.append('Onions')
# print(grocery_list)
# grocery_list.insert(1,'Pickle')
# print(grocery_list)
# grocery_list.remove('Pickle')
# print(grocery_list)
# grocery_list.sort()
# print(grocery_list)
# grocery_list.reverse()
# print(grocery_list)
# del grocery_list[3]
# print(grocery_list)
# del grocery_list[3]
# print(grocery_list)
# to_do_list_2 = other_events + grocery_list
# print(len(to_do_list_2))
# print(max(to_do_list_2))
# print(min(to_do_list_2))

# pi_tuple = (3,2,4,5,3,56,3)
#
# new_tuple = list(pi_tuple)
# new_list = tuple(new_tuple)

import random
import  sys
import os

# super_villains = {'Fiddler' : 'Isaac Bowin',
#                   'Captain Cold' : 'Leonard Snart',
#                   'Weather Wizard' : 'Mark Mardon',
#                   'Mirror Master' : 'Sam Scudder',
#                   'Pied Piper' : 'Thomas Peterson'}

# print(super_villains['Captain Cold'])
#
# del super_villains['Fiddler']
#
# print(super_villains)
#
# super_villains['Pied Piper'] = 'Viktor'
# print(super_villains['Pied Piper'])
# # print(len(super_villains))
# # print(super_villains.get("Pied Piper"))
# print(super_villains.keys())
# print(super_villains.values())
#
# # if else elif == != > >= <=
#
# age = 31
#
# if age > 16 :
#     print('You are old enough to drive')
# else:
#     print('You are not old enough to drive')
#
# if age >= 21:
#     print('You are old enough to drive a tractor or trailer')
# elif age >= 16:
#     print('You are old enough to drive a car')
# else: print('You are not old enough to drive')
#
# if((age > 1) and (age <= 18)):
#     print('You  get a birthday')
# elif (age == 21) or (age >= 65):
#     print('You get a birthday second time')
# elif not(age == 30):
#     print("You don't get a birthday")
# else:
#     print('You get a birthday anyway')


#
# for x in range(0, 10):
#     print(x, " ", end="")
# print('\n')
#
# grocery_list = ['juice', 'Tomatoes', 'Potatoes', 'Bananas']
#
# for y in grocery_list:
#     print(y)
#
# for x in [2,3,4,5,6,7,8]:
#     print(x)
# num_list = [[1,2,3],[10,20,30],[100,200,300]]
# for x in range(0,3):
#     for y in range(0,3):
#         print(num_list[x][y])                                 # не соввсем понимаю каким образом это работает?
#

#
# random_num =  random.randrange(0,100)
#
# while(random_num !=15):
#     print(random_num)
#     random_num = random.randrange(0, 100)                      # не понятно почему без этой строки не работает  цикл

# i = 0;
#
# while(i <=20):
#     if(i%2 ==0):
#         print(i)
#     elif(i==11):
#         break
#     else:
#         i +=1
#         continue
#     i +=1

# def addNumber(fNum, lNum):
#     sumNum = fNum + lNum
#     return sumNum
# string = addNumber(1,141)
# print(string)
                                                                 # как прыгать в начало и конец файла? hotkeys
# print('What is your name')
# name = sys.stdin.readline()
# print("Hello", name)
#
# long_string = "I'll catch you if you fall -  The Floor"
#
# print(long_string[0:4])
# print(long_string[-5:])
# print(long_string[:-5])
# print(long_string[:4] + " be there")
# print(long_string.capitalize())
# print(long_string.find("Floor"))
# print(long_string.isalpha())
# print(long_string.isalnum())
# print(len(long_string))
# print(long_string.replace('Floor', 'Grooound'))
# print(long_string.strip())
# quote_list  = long_string.split(" ")
# print(quote_list)

# test_file = open("test.txt", "wb")
# print( test_file.mode)
# print(test_file.name)
# test_file.write(bytes("Write me to the file \n", 'UTF-8'))
# test_file.close()
# test_file = open("test.txt", "r+")
# text_in_file = test_file.read()
# print(text_in_file)
# os.remove("test.txt")
                                                             # set and get сеттеры и геттеры простыми словами?
#
# class Animal:
#     _name = ""
#     _height = 0
#     _weight = 0
#     _sound = 0
#
#     def __init__(self, name, height, weight, sound):
#         self._name = name
#         self._height = height
#         self._weight = weight
#         self._sound = sound
#
#     def set_name(self, name):
#         self._name = name
#
#     def get_name(self):
#         return self._name
#
#     def set_height(self, height ):
#         self._height = height
#
#     def get_height(self):
#         return self._height
#
#     def set_weight(self, weight):
#         self._weight = weight
#
#     def get_weight(self):
#         return self._weight
#
#     def set_sound(self, sound):
#         self._sound = sound
#
#     def get_sound(self):
#         return self._sound
#
#     def get_type(self):
#         return("Animal")
#
#     def toString(self):
#         return "{} is {} cm tall and {} kilograms and say {}".format(self._name,
#                                                                      self._height,
#                                                                      self._weight,
#                                                                      self._sound)
# cat = Animal('Whiskers', 10, 33, "Meow")
# print(cat.toString())
#
# class Dog(Animal):
#     __owner = ""
#
#     def __init__(self, name, height, weight, sound, owner):
#         self._owner = owner
#         super(Dog, self).__init__(name, height, weight, sound)
#
#     def set_owner(self, owner):
#         self._owner = owner
#
#     def get_owner(self):
#         return self._owner
#
#     def get_type(self):
#         print("Dog")
#
#     def toString(self):
#         return "{} is {} cm tall and {} kilograms and say {}. His owner is {}".format(self._name,
#                                                                                       self._height,
#                                                                                       self._weight,
#                                                                                       self._sound,
#                                                                                       self._owner)
#
#     def multiple_sound(self, how_many =None):
#         if how_many is None:
#             print(self.get_sound())
#         else:
#             print(self.get_sound() * how_many)
# spot = Dog("Spot", 11, 22, "Ruff", "Derek")
# print(spot.toString())                                           #также не могу понять почему это не работает
#
# dog = Dog('Buddy', 11, 20, "Gaw", "Viktor")
# print(dog.toString())
#
# class AnimalTesting:
#     def get_type(self, animal):
#         animal.get_type()
#
# test_animals = AnimalTesting()
#
# test_animals.get_type(cat)                           # и это не работает(((( по видео должно написать в консоле Animal
# test_animals.get_type(spot)                          # и это не работает(((( по видео должно написать в консоле Dog 42min видео
#
# spot.multiple_sound(4)
#

string = "i love Python"
print(string.capitalize())

print(string.zfill(3))          #не понятно что этот метод делает
print(string.casefold())
print(string)
print(string.count("f"))            #метод вроде бы должен возвращать количесвто встретившихся значений но почему то не работает
print(string.encode())
print(string.endswith("e"))
print(string.expandtabs(3))
x = string.encode()
print(x)


y = "i\t lov\te Python"
y = y.expandtabs(2)
print(y)

txt = "Hello, welcome to my world."

c = txt.find("o", 5, 20)

print(c)

v = "For only {price:.2f} dollars!"
print(v.format(price = 4))

b = string.index("Py")

print(b)