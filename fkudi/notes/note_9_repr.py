

class Cooffe:

    milk = 100
    coffe = 15
    water = 200

    def __str__(self):
        return "My Greaty Coffe with volume {}".format(self.milk + self.water + self.coffe)

    def __repr__(self):
        return "Cooffe()"

x = Cooffe()

print(repr(x))
print(str(x))


name = "John"
x = "Hello " + name + " how are you."


x = "Hello %s how are you." % name

x = "Hello {} how are you.".format(name)
x = "Hello {0} how are you.".format(name)
x = "Hello {name} how are you.".format(name=name)

x = f"Hello {name} how are you."
