"""
Дана функция, которая генерирует и возвращает случайное значение, если значение больше 0.5 то падает с ошибкой.

```
def gen_random():
    import random
    x = random.random()
    assert x <= 0.5
    return x
```

Задания:
1. Нужно написать декоратор, который бы позволил делать повторную попытку вызова функции пока она не сгенерирует валидное значение.
2. Нужно написать параметризированный декоратор, в котором можно задать число повторных попыток

Результат:
1. Обычный декоратор
```
def retry(func: callable) -> callable:   .


@retry
def gen_random():
    import random
    x = random.random()
    assert x <= 0.5
    return x
```

2. Параметризированный декоратор:
```
def retry(retries: int) -> callable:   .
в итоге получится что то вроде:

параметризированный декоратор:
```
def retry(retries: int) -> callable:   .


@retry(5)
def gen_random():
    import random
    x = random.random()
    assert x <= 0.5
    return x
"""


# def retry(func: callable) -> callable:
#     def wrapper():
#         while True:
#             try:
#                 return func()
#             except AssertionError:
#                 pass
#     return wrapper


def parametrised_retry(retries):
    def retry(func: callable):
        def wrapper():
            nonlocal retries
            while True:
                try:
                    return func()
                except AssertionError:
                    retries -= 1
                    if retries == 0:
                        raise AssertionError
        return wrapper
    return retry


@parametrised_retry(5)
def gen_random():
    import random
    x = random.random()
    assert x <= 0.5
    return x


print(gen_random())
