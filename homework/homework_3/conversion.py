
int("123")
int(123.0)
int("10110101", 2)
int("0b10110101", 2)
int("10110101", 2)

float("123")
float(123.0)
float(123)

str(123)
str(123.0)
str(True)
str(None)


list("abc")
list({"a": 1, "b": 2})
list((1, 2, 3))
list({"a", "b"})
list(range(10))
list(enumerate(["a", "b", "c"]))
list(zip(["a", "b", "c"], [1, 2, 3]))
list({"a": 1, "b": 2}.keys())
list({"a": 1, "b": 2}.values())
list({"a": 1, "b": 2}.items())

tuple("abc")
tuple({"a": 1, "b": 2})
tuple((1, 2, 3))
tuple({"a", "b"})

set("abc")
set({"a": 1, "b": 2})
set((1, 2, 3))
set({"a", "b"})

dict(a=123, b=456)
dict([("a", 123), ("b", 456)])
dict({"a": 1, "b": 2})
dict(enumerate(["a", "b", "c"]))
dict(zip(["a", "b", "c"], [1, 2, 3]))
dict({"a": 1, "b": 2}.items())
