import os
import sys

print(os.environ.get("FOO"))
print(sys.argv)


try:
    while True:
        data = input()
        print("from python program ", data)
except KeyboardInterrupt:
    print("grace full stop")
except EOFError:
    print("all processed")
