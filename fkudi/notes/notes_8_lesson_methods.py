

class MyGreatClass:

    x = 1234

    def my_method(self):
        print(self)





item1 = MyGreatClass()
item2 = MyGreatClass()




item1.my_method()
# 1.   receive obj by ref name  'item1'
# 2.   receive obj by ref name 'my_method' from obj discovered on 1 step
# 3.   make a call to object discovered from 2 step

step_1 = item1
step_2 = step_1.my_method    # method still remembers object whom it belongs
step3 = step_2()


print(MyGreatClass.my_method)  # simple func
print(item1.my_method)         # method belongs to item1
print(item2.my_method)         # method belongs to item2


a = MyGreatClass.my_method    # func
b = item1.my_method           # obj method


# a()   # error , required param self
b()


MyGreatClass.my_method(item1)
MyGreatClass.my_method(item2)






item1.my_method()

c = type(item1)
f = c.my_method
f(item1)

type(item1).my_method(item1)




