class Person:
    _instances = []

    def __new__(cls, name, age, occupation):
        instance = super(Person, cls).__new__(cls)
        cls._instances.append(instance)
        return instance

    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Occupation: {self.occupation}"

    @classmethod
    def get_instances(cls):
        return cls._instances
