from olpopova.homework.homework09.overriding_new import MyClass


def test_remembering_created_instances():
    assert len(MyClass.objects) == 0

    instance1 = MyClass()
    instance2 = MyClass()
    instance3 = MyClass()

    assert len(MyClass.objects) == 3
    assert instance1 in MyClass.objects
    assert instance2 in MyClass.objects
    assert instance3 in MyClass.objects
    assert len(vars(instance1)) == 0             # __init__ wasn`t called because of overriding __new__
