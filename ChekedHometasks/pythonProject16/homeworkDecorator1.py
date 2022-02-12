"""Напишите функцию декоратор, которая добавляет 1 к заданному числу"""


def decorator(func):
    def wrapper():
        result = func()
        print(result + 1)
        return result

    return wrapper


@decorator
def input_number():
    converted_num = 7
    return converted_num


input_number()
