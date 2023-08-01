from sys import argv


path, operator, value = argv

while True:
    value = float(value)
    received = float(input())

    if operator == "+":
        res = received + value
    elif operator == "-":
        res = received - value
    elif operator == "*":
        res = received * value
    elif operator == "/":
        res = received / value

    print(res)
