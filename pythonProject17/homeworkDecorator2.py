"""Напишите функцию декоратор, которая переводит полученный текст в верхний регистр"""


def decorator(func):
    def wrapper():
        result = func()
        result = result.upper()
        print(result)
        return result

    return wrapper


@decorator
def input_number():
    converted_num = input("Enter the string")
    print(converted_num)
    return converted_num


input_number()
