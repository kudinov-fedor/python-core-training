# Verify in Python Console conversion of objects

type(enumerate(["a", "b", "c"]))  # <class 'enumerate'>
str(enumerate(["a", "b", "c"]))  # '<enumerate object at 0x0000025C453FAC00>'
list(enumerate(["a", "b", "c"]))  # [(0, 'a'), (1, 'b'), (2, 'c')] -> tests

type(zip(["a", "b", "c"], [1, 2, 3]))  # <class 'zip'>
str(zip(["a", "b", "c"], [1, 2, 3]))  # '<zip object at 0x0000025C4541CD80>'
list(zip(["a", "b", "c"], [1, 2, 3]))  # [('a', 1), ('b', 2), ('c', 3)]  -> tests

type(range(10))  # <class 'range'>
str(range(10))  # 'range(0, 10)'
list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

type(frozenset({"apple", "banana", "cherry"})) # <class 'frozenset'>
str(frozenset({"apple", "banana", "cherry"})) # "frozenset({'apple', 'banana', 'cherry'})"
list(frozenset({"apple", "banana", "cherry"}))  # ['apple', 'banana', 'cherry']

type(bytearray(b'\x00\x00\x00\x00\x00')) # <class 'bytearray'>
str(bytearray(5)) # "bytearray(b'\\x00\\x00\\x00\\x00\\x00')"
list(bytearray(5))  # [0, 0, 0, 0, 0]

memoryview(bytes(5))  # <memory at 0x0000025C45383640>
str(memoryview(bytes(5)))  # '<memory at 0x0000021BCCEB3640>'
list(memoryview(bytes(5)))  # [0, 0, 0, 0, 0]


def generate_integer():
    yield int("10110101", 2)  # 181
    yield int("0b10110101", 2)  # 181
    yield int(True)  # 1
    yield int(False)  # 0


def generate_float():
    yield float(True)  # 1.0
    yield float(False)  # 0.0


def generate_complex():
    yield complex(True)  # (1+0j)
    yield complex(False)  # 0j
    yield complex(5)  # (5+0j)


def generate_string():
    yield str(True)  # 'True'
    yield str(None)  # 'None'
    yield str({"a": 1, "b": 2})  # "{'a': 1, 'b': 2}"


def generate_list():
    yield list("abc")  # ['a', 'b', 'c']
    yield list({"a": 1, "b": 2})  # ['a', 'b']
    yield list((1, 2, 3))  # [1, 2, 3]
    yield list({"a", "b"})  # ['a', 'b']
    yield list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    yield list(enumerate(["a", "b", "c"]))  # [(0, 'a'), (1, 'b'), (2, 'c')] -> tests
    yield list(zip(["a", "b", "c"], [1, 2, 3]))  # [('a', 1), ('b', 2), ('c', 3)]  -> tests
    yield list({"a": 1, "b": 2}.keys())  # ['a', 'b']
    yield list({"a": 1, "b": 2}.values())  # [1, 2]
    yield list({"a": 1, "b": 2}.items())  # [('a', 1), ('b', 2)] -> tests


def generate_tuple():
    yield tuple("abc")  # ('a', 'b', 'c')
    yield tuple({"a": 1, "b": 2})  # ('a', 'b')
    yield tuple((1, 2, 3))  # (1, 2, 3)
    yield tuple({"a", "b"})  # ('a', 'b')


def generate_set():
    yield set("abc")  # {'c', 'a', 'b'}
    yield set({"a": 1, "b": 2})  # {'a', 'b'}
    yield set((1, 2, 3))  # {1, 2, 3}
    yield set({"a", "b"})  # {'a', 'b'}


def generate_dict():
    yield dict(a=123, b=456)  # {'a': 123, 'b': 456}
    yield dict([("a", 123), ("b", 456)])  # {'a': 123, 'b': 456}
    yield dict({"a": 1, "b": 2})  # {'a': 1, 'b': 2}
    yield dict(enumerate(["a", "b", "c"]))  # {0: 'a', 1: 'b', 2: 'c'} -> tests
    yield dict(zip(["a", "b", "c"], [1, 2, 3]))  # {'a': 1, 'b': 2, 'c': 3}
    yield dict({"a": 1, "b": 2}.items())  # {'a': 1, 'b': 2}


if __name__ == '__main__':
    print('Generated integer')
    for value in generate_integer():
        print(value)

    print('Generated float')
    for value in generate_float():
        print(value)

    print('Generated complex')
    for value in generate_complex():
        print(value)

    print('Generated string')
    for value in generate_string():
        print(value)

    print('Generated list')
    for value in generate_list():
        print(value)

    print('Generated tuple')
    for value in generate_tuple():
        print(value)

    print('Generated set')
    for value in generate_set():
        print(value)

    print('Generated dictionary')
    for value in generate_dict():
        print(value)
