import pytest

from olpopova.homework.homework09.overriding_new import MyClass, Other


def test_remembering_created_instances():
    assert len(MyClass.objects) == 0

    instance1 = MyClass()
    instance2 = MyClass()
    instance3 = MyClass()

    assert len(MyClass.objects) == 3
    assert instance1 in MyClass.objects
    assert instance2 in MyClass.objects
    assert instance3 in MyClass.objects
    assert len(vars(instance1)) == 1
    assert len(vars(instance2)) == 1


def test_ignoring_init():
    assert len(Other.objects) == 0

    instance1 = Other()
    instance2 = Other()

    assert len(Other.objects) == 2
    assert instance1 in Other.objects
    assert instance2 in Other.objects
    with pytest.raises(TypeError):
        assert len(vars(instance1)) == 1
