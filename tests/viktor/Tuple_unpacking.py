# a, b, c, d, *e, f, g = range(21)
# print(len(e))
#
# print(e)



# for i in range(10):
#    if i > 7:
#       print(i)
#       break
# else:
#    print("7")
#


try:
  print(1)
  print(1 + "1" == 2)
  print(2)
except TypeError:
  print(3)
else:
  print(4)
