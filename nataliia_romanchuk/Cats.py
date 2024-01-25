class Cats:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        return f"Cat {self.name} says Meow for " + f"{self.age} years!"

    def sleep(self):
        return f"Cat {self.name} is sleeping. Shhhhhhhh!"

