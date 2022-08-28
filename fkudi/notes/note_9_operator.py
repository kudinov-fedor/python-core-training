x = 3
y = ["a", "b"]


# x * y
print("x.__mul__(y)  =   ", x.__mul__(y))
# if NotImplemented
print("y.__rmul__(x)  =   ", y.__rmul__(x))
