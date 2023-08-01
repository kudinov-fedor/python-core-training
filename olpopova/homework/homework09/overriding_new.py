class MyClass:
    objects = []

    def __new__(cls):
        item = super().__new__(cls)
        cls.objects.append(item)
        return item

    def __init__(self):
        a = 'ghj'
