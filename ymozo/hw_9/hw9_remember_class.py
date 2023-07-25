class RememberObject:
    _instances = []

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        cls._instances.append(instance)
        return instance

    @classmethod
    def get_all_instances(cls):
        return cls._instances


class Cars(RememberObject):

    def __init__(self, car_manuf, model):
        self.car_manuf = car_manuf
        self.model = model

    def car_info(self):
        print(f"Car brand: {self.car_manuf}, model: {self.model}")


car1 = Cars("Mazda", "Cx-5")
car2 = Cars("Toyota", "Highlander")
car1.car_info()
car2.car_info()


all_instances = RememberObject.get_all_instances()
print(len(all_instances))
