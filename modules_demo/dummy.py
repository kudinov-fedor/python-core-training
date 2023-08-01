
try:
    while True:
        item = input()
        print(item)
except (KeyboardInterrupt, EOFError):
    print("gracefull stop")


print("exit")
