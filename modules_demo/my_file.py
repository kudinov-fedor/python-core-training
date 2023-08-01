from executable_module.some_other_module import a
from executable_module.some_other_module import a
from executable_module.some_other_module import a
from executable_module.some_other_module import a
from executable_module.some_other_module import a
from executable_module.some_other_module import a



print(a)

print(__name__)



import sys


print("\nPATH")
for p in sys.path:
    print(p)


print("\n MODULES:")
for m in sys.modules:
    print(m)
