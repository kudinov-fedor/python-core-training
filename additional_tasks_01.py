
# print-----------------------------------------------------------
# данный код
name = "Иван"
surname = "Петров"
salary = "90 000"
# требуемый вывод:
# Иван Петров зарабатывает 90 000 рублей
# first solution
  print(name, surname, end=' зарабатывает ')
  print(salary, end=' рублей' )
# second solution
  print(name, surname, "зарабатывает", salary, "рублей", sep=' ')


# list -----------------------------------------------------------
# 1. Создайте пустой список, определите его тип и выведите в консоль.
# данный код:
# gift_list=
# answer_1=
# print(answer_1)
# требуемый вывод:
# <class 'list'>
# solution
def test_list_type():
    gift_list = []

    assert type(gift_list) is list
    assert isinstance(gift_list, list)
    assert issubclass(type(gift_list), list)

    return type(gift_list)

print(test_list_type())

# 2. Допишите код, чтобы gift_list был заполненным кортежем. Порядок элементов значения не имеет.
gifts=
print(gifts)
# требуемый вывод:
# ("Камера", "Наушники", "Часы")
#solution:
gifts=("Камера", "Наушники", "Часы")

#3 Допишите код, что бы вывести последний элемент списка.
# данный код
sample = ["abc", "xyz", "aba", 1221]
# требуемый вывод:
# 1221
#solution
print(sample[-1])

#4. Допишите код, что бы вывести расширенный список.
# данный код
sample = ["Green", "White", "Black"]
print(sample)
# требуемый вывод:
# ["Red", "Green", "White", "Black", "Pink", "Yellow"]
решение
sample = ["Green", "White", "Black"]
sample.insert(0, "Red")
sample.append("Pink")
sample.append("Yellow")
print(sample)

#5. Исправьте ошибки в коде, что бы посчитать сумму элементов в списке.
# данный код
sample = ["11", "33", "50"]
print(sample.sum())
# требуемый вывод:
# 94
решение
sample = [11, 33, 50]
print(sum(sample))


# Dictionary-----------------------------------------------------------
# 1. Выведите значение возраста из словаря person.
# данный код
person = {"name": "Kelly", "age":25, "city": "New york"}
# требуемый вывод:
# 25
#solution
print(person.get("age"))

# 2. Исправьте ошибки в коде, что бы получить требуемый вывод.
# данный код
d1 = {"a": 100. "b": 200. "c":300}
d2 = {a: 300, b: 200, d:400}
print(d1["b"] == d2["b"])
# требуемый вывод:
# True
#solution
d1 = {"a": 100, "b": 200, "c":300}
d2 = {"a": 300, "b": 200, "d":400}
