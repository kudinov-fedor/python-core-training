


class Square:

    # presetup of object just after it was created
    def __init__(self, param1=5):
        print("I am a great hook to setup object", self)
        self.side = param1     # obj attr

    # nothing before

    def get_square(self):
        return self.side ** 2

    # nothing after


# inheritance
class Circle(Square):

    # def get_square(self):
    #     return self.side ** 2 * 3.14

    def get_square(self):
        res = super().get_square()
        return res * 3.14



x = Square(10)
print(x.side)


y = Square(9)
print(y.side)

z = Square()
print(z.side)


print(x.get_square())
print(y.get_square())
print(z.get_square())



a = Circle(5)
print(a)
print(a.get_square())





print(isinstance(Circle, type))
