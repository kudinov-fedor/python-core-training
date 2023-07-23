"""
Create class, which would remember all created objects (override __new__)
"""


class MyClass:
    container = []

    def __new__(cls, username):
        """
        This method creates new object with 'Username' parameter
        """
        new_obj = super(MyClass, cls).__new__(cls)
        new_obj.username = username
        cls.container.append(username)
        return cls.container


if __name__ == '__main__':
    emp1 = MyClass(username="Test1")
    emp2 = MyClass(username="Test2")
    emp3 = MyClass(username="Test3")
    print(MyClass.container)
