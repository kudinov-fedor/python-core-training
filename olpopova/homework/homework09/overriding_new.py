class MyClass:
    objects = []

    def __new__(cls):
        item = super().__new__(cls)
        cls.objects.append(item)
        return item

    def __init__(self):
        self.a = 'ghj'


class Other:
    objects = []

    def __new__(cls):
        cls.objects.append(123)
        return 123

    def __init__(self):
        self.a = 'ghj'
