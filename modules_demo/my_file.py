import sys

# sys.path.append("/Users/fkudi/PycharmProjects/python-core-training/modules_demo/executable_module")



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
