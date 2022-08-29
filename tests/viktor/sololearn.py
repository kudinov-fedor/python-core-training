#
# car = {
#     'brand':'BMW',
#     'year':2018,
#     'color': 'red',
#     'mileage': 15000
# }
# a = input()
# print(car[a])


# cart = [15, 42, 120, 9, 5, 380]
#
# discount = int(input())
# total = 0
# for x in cart:
#     total = total + x
# print(total)
#
# total1 = 0
# for x in cart:
#     total1 = total1 + (x - x*discount/100)
# print(total1)



# ***************SUM of the numbers *********************
# N = int(input())
# lt = list(range(0, N + 1))
# sum = 0
# for i in lt:
#     sum = sum + i
# print(sum)



# data = [7, 5, 6.9, 1, 8, 42, 33, 128, 1024, 2, 8, 11, 0.4, 1024, 66, 809, 11, 8.9, 1.1, 3.42, 9, 100, 444, 78]
# print(len(data))
# data.remove(min(data))
# data.remove(max(data))
# print(len(data))
# sum = 0
# for i in data:
#     sum = sum + i
# print(sum)



# text = input()
# word = input()
#
# def search(text, word):
#     if word in text:
#         print("Word found")
#     else:
#         print("Word not found")
#
# print(search(text, word))

#
# try:
#   print(1 / 0)
# except ZeroDivisionError:
#   raise ValueError


# num = input(':')
# if float(num) < 0 :
#     raise ValueError('Negative!')
# else:
#     print('Positive')


# def some_func():
#     print(('Hi'))
# #     return 'End'
# # some_func()
# print(some_func())


# What number does this code print?
# foo = print()
# if foo == None:
#    print(1)
# else:
#    print(2)


# List comprehension
#
# list = [x *10 for x in range(5, 9)]
# print(list)


# String functions

# print(", ".join(["spam", "eggs", "ham"]))
# #prints "spam, eggs, ham"
#
# print("Hello ME".replace("ME", "world"))
# #prints "Hello world"
#
# print("This is a sentence.".startswith("This"))
# # prints "True"
#
# print("This is a sentence.".endswith("sentence."))
# # prints "True"
#
# print("This is a sentence.".upper())
# # prints "THIS IS A SENTENCE."
#
# print("AN ALL CAPS SENTENCE".lower())
# #prints "an all caps sentence"
#
# print("spam, eggs, ham".split(", "))
# #prints "['spam', 'eggs', 'ham']"



#Text Analyzer
# def count_char(text, char):
#    count = 0
#    for c in text:
#       if c == char:
#          count += 1
#    return count
#
#
# file = open("newfile.txt", "w")
# file.write("""Ornhgvshy vf orggre guna htyl.
# Rkcyvpvg vf orggre guna vzcyvpvg.
# Fvzcyr vf orggre guna pbzcyvpngrq.
# Syng vf orggre guna arfgrq.
# Fcenfr fv orggre guna qrafr.
# Ernqnovyvgl pbhagf.
# Fcrpvny pnfrf nera'g fcrpvny rabthu gb oernx gur ehyrf.
# Nygubhtu cenpgvpnyvgl orgnf chevgl.
# Reebef fubhyq arire cnff fvyragyl.
# Hayrff rkcyvpvgyl fvyraprq.
# Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba bg thrff.
# Gurer fubhyq or bar-- naq cersrenoylbayl bar --boivbhf jnl gb qb vg.
# Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.
# Abj vf orggre guna arrire.
# Nygubhtu arire vf bsgra orggre guna *evtug* abj.
# Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
# Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.
# Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!""")
# file.close()
# filename = "newfile.txt"
# with open(filename) as f:
#    text = f.read()
#
# for char in "abcdefghijklmnopqrstuvwxyz":
#    perc = 100 * count_char(text, char) / len(text)
#    print("{0} - {1}%".format(char, round(perc, 2)))


#Longest Word
#Given a text as input, find and output the longest word.

#this is an awesome text
# txt = input()
# result=txt.split(" ")
# num=max(result,key=len)
# print(num)


# ### LAMBDA ##########
# triple = lambda x: x * 3
# add = lambda x, y: x + y
# print(add(triple(3), 4))


# nums = 11, 22, 33, 44
# x = list(map(lambda l: l * 2 , nums))
# print(x)

################################## ?????
# numsl = 11
# x = lambda l: l * 2 , numsl
# print(x)


# Filter
# nums = [11, 22, 33, 44, 55, 88]
# res = list(filter(lambda x: x%2==0, nums))
# print(res)



# ##################
# names = ["David", "John", "Annabelle", "Johnathan", "Veronica"]
#
# filt = list(filter(lambda x: len(x) > 5, names))
# print(filt)


##########################
# nums = [1, 2, 3, 6, 7, 8, 9]
# fltr = list(filter(lambda x: x < 5, nums))
# print((fltr))

# import sys
# def return_list():
#     return list(range(100_000,1,-1))
# ### Generators
# def countdown():
#    i = 100_000
#    while i > 0:
#       yield i
#       i -= 1
# a = return_list()
# b = countdown()
#
# print(sys.getsizeof(a))
# print(sys.getsizeof(b))
# #
#
# for i in countdown():
#    print(i)
# print(countdown())
# a = countdown
# print(a())
# print(next(a))
# print(next(a))


# def infinite_sevens():
#    while True:
#       yield 7
#
#
# for i in infinite_sevens():
#    print(i)

#####

#
# def is_prime(num: int):
#     return num % 2 == 0
#
# def get_prime():
#    num = 2
#    while True:
#       if is_prime(num):
#          print(num)
#          yield num
#       num += 1
#
#
# for i in get_prime():
#     pass


# def numbers(x):
#    for i in range(x):
#       if i % 2 == 0:
#          yield i
#
#
# print(list(numbers(111)))



# txt = input()
# def words():
#     for i in txt.split():
#             yield i
#     #your code goes here
#
# print(list(words()))


# def make_word():
#     word = ''
#     for i in 'spampararam tam':
#         word += i
#         yield word
#
#
# print(list(make_word()))

######## Decorators ############

# def decor(func):
#   def wrap():
#     print("=========+++++++======")
#     func()
#     print("=========+++++++======")
#   return wrap
#
# def print_text():
#   print("Hello world of Python!")
#
# decorated = decor(print_text)
# decorated()


# def decor(func):
#   def wrap():
#     print("=========+++++++======")
#     func()
#     print("=========+++++++======")
#   return wrap
#
#
# def print_text():
#   print("Hello world of Python!!!")
#
# print_text = decor(print_text)
# print_text();


# def decor(func):
#   def wrap():
#     print("=========+++++++======")
#     func()
#     print("=========+++++++======")
#   return wrap
#
# @decor
# def print_text():
#   print("Hello world of Python!!!")
#
# print_text();


# text = input()
#
#
# def uppercase_decorator(func):
#     def wrapper(text):
#         return func(text).upper()
#         # your code goes here
#
#     return wrapper
#
#
# @uppercase_decorator
# def display_text(text):
#     return (text)
#
#
# print(display_text(text))


############# Recursion
# def calc(list):
#     if len(list)==0:
#         return 0
#     else:
#         return list[0] **2 + calc(list[1:])
#
# list = [1, 3, 4, 2, 5]
# x = calc(list)
# print(x)


#########  itertools

# from itertools import takewhile
# nums = [2, 4, 6, 8, 7, 9, 8, 8]
# a = takewhile(lambda x: x% 2== 0, nums)
# print(list(a))


# ######## Fibonacci
n = int(input())


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n - 1) + fibonacci(n - 2))
if n <= 0:
    print('Please enter a positive int')
else:
    print('Fibonacci sequence:')
    for i in range(n):
        print(fibonacci(i))
#

#Python program to display the Fibonacci sequence

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 12

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))


fibonacci(4)
from selenium.common.exceptions import (ElementNotInteractableException,
                                        NoSuchElementException)
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
#
# driver = webdriver.ChromeOptions()
# options = Options()
# options.add_experimental_option("excludeSwitches", ["enable-logging"])
# driver.add_experimental_option("prefs", prefs)
# driver = webdriver.Chrome(service=Service(
#     ChromeDriverManager().install()), options=options)


# class A:
#     def spam(self):
#         print(1)
#
# class B(A):
#     def spam(self):
#         print(2)
#         super().spam()
#
# B().spam()