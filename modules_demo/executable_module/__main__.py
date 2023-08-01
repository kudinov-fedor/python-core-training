
print("executable module main is executed")

print(__name__)



from some_other_module import a
print(a)




import sys


print("\nPATH")
for p in sys.path:
    print(p)


print("\n MODULES:")
for m in sys.modules:
    print(m)
