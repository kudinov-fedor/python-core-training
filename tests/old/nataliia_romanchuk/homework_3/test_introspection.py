import logging

import pytest
import types

# --- Підготовка об'єктів (копіюємо з вашої домашки) ---
some_bool = bool()
some_int = int()
some_float = float()
some_str = str()
some_tuple = tuple()
some_list = list()
some_range = range(10)
some_set = set()
some_dict = dict()

some_lambda = lambda: 1


def some_func():
    return 1


def some_gen_func():
    yield 1
    yield 2
    yield 3


class SomeClass:
    """my great docstring"""
    class_atr = 123

    def __init__(self):
        self.instance_attr = 987


some_object = SomeClass()

def some_error():
    try:
        5 / 0
    except ZeroDivisionError as error:
        some_error = error
        print(f"Found: {some_error}")

def some_error1():
    try:
        5 / 0
    except ZeroDivisionError:
        logging.exception("Сталася помилка під час обчислень")


def test_type_checks():
    # Types verification and comparison with 'is'
    assert type(some_bool) is bool
    assert type(some_bool) is not int  # type() строго перевіряє тип
    assert type(some_bool) is not str
    assert (type(some_bool) in (str, bool)) is True

    # Перевірка типів складніших об'єктів
    assert type(some_lambda) is types.LambdaType
    assert type(some_func) is types.FunctionType
    assert type(
        some_gen_func) is types.FunctionType  # сама функція — це FunctionType, а її виклик поверне GeneratorType
    assert type(some_object) is SomeClass
    assert type(some_error) is not ZeroDivisionError


def test_isinstance():
    # bool є підкласом int в Python!
    assert isinstance(some_bool, bool) is True
    assert isinstance(some_bool, int) is True
    assert isinstance(some_bool, float) is False
    assert isinstance(some_bool, (int, float, str)) is True

    # Винятки (Exceptions) теж успадковуються
    assert isinstance(some_error, ZeroDivisionError) is False
    assert isinstance(some_error, Exception) is False

    # Мета-типи: все в Python є об'єктом (object), але не все є типом (type)
    assert isinstance(some_bool, object) is True
    assert isinstance(some_bool, type) is False
    assert isinstance(bool, type) is True
    assert isinstance(bool, object) is True


def test_issubclass():
    # Перевірка зв'язків між класами
    assert issubclass(bool, bool) is True
    assert issubclass(bool, int) is True  # Знову ж таки, bool наслідується від int
    assert issubclass(bool, float) is False
    assert issubclass(ZeroDivisionError, ArithmeticError) is True
    assert issubclass(ZeroDivisionError, Exception) is True


def test_lengths():
    assert len(some_str) == 0
    assert len(some_dict) == 0
    assert len(some_list) == 0
    assert len(some_tuple) == 0
    assert len(some_set) == 0
    assert len(some_range) == 10


def test_callable():
    # Перевірка чи можна "викликати" об'єкт (навісити дужки `()`)
    assert callable(some_bool) is False
    assert callable(bool) is True  # Класи можна викликати (створює об'єкт)
    assert callable(some_func) is True
    assert callable(some_gen_func) is True
    assert callable(some_lambda) is True
    assert callable(SomeClass) is True  # Сам клас — викликаємий
    assert callable(some_object) is False  # Об'єкт класу не викликаємий, бо немає методу __call__


def test_identity_and_equality():
    a = (1, 2, 3)
    b = (1, 2, 3)

    assert (a == b) is True  # Значення однакові
    # Оператор 'is' перевіряє id в пам'яті. Для незмінних кортежів Python
    # може оптимізувати пам'ять і дати однаковий id, а може й ні (залежить від запуску).
    # Зазвичай для однакових літералів у коді:
    assert (a is b) is True
    assert (hash(a) == hash(b)) is True  # Якщо об'єкти рівні, їх хеші однакові
    assert (id(a) == id(b)) is True  # Оскільки a is b, то і id однакові


def test_attributes_and_introspection():
    # hasattr перевіряє наявність атрибутів або методів
    assert hasattr(some_list, "append") is True
    assert hasattr(some_object, "instance_attr") is True
    assert hasattr(some_object, "class_atr") is True  # Об'єкт бачить атрибут класу
    assert hasattr(SomeClass, "class_atr") is True
    assert hasattr(SomeClass,
                   "instance_attr") is False  # Клас НЕ бачить атрибут, який створюється лише в __init__ об'єкта

    # vars() повертає __dict__ об'єкта (його власні змінні)
    assert vars(some_object) == {"instance_attr": 987}
    assert "class_atr" in vars(SomeClass)

    # Документація docstring
    assert "my great docstring" in some_object.__doc__


def test_repr_vs_str():
    # str() робить рядок для людей, repr() — технічний рядок для розробників
    assert str("123") == "123"
    assert str(123) == "123"

    assert repr("123") == "'123'"  # repr додає лапки всередину навколо рядка
    assert repr(123) == "123"
