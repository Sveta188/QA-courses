"""Напишите декоратор change, который делает так, что задекорированная
функция принимает все свои не именованные аргументы в порядке, обратном тому, в котором их передали"""


def decorator(func):
    def wrapper(*args, **kwargs):
        args = reversed(args)
        func(*args, **kwargs)

    return wrapper


@decorator
def input_arguments(x, y):
    print(x, y)
    result = x - y
    print(result)
    return result


input_arguments(10, 20)

