import math
import random
import sys


class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


number1 = ""
number2 = ""
operator = ""
result = 0


def operations():
    print("+...Addition")
    print("- ... Subtraction")
    print("*... Multiplication")
    print("/ ...Division")
    print("root...Root, please enter the second number in fractional format")
    print("^...Square")


def input_numbers(text):
    converted_num = math.nan

    while True:
        num = input(text)
        try:
            # Parse the num to float.
            float(num)
        except ValueError:
            print("Please, enter the number")
        else:
            converted_num = float(num)
            break
    return converted_num


while True:
    print(Color.BOLD + "The list of abilities for calculator" + Color.END)
    while True:
        operator = input("Enter the operator, if you want to see all offered operations - type help\n"
                         "If you want to exit- type exit: ")
        if operator == "help":
            operations()
        elif operator == "exit":
            sys.exit()
        elif operator == "+" or operator == "/" or operator == "-" \
                or operator == "*" or operator == "root" or operator == "^":
            break
        else:
            print("Error, try again")
    number1 = input_numbers("Enter the first number")
    while True:

        number2 = input_numbers("Enter the second number")
        if operator == "/" and number2 == 0:
            print("Error! You try to divide on 0!")

        else:
            break
    if operator == "+":
        result = number1 + number2
        print("Your result is", result)
    elif operator == "-":
        result = number1 - number2
        print("Your result is", result)
    elif operator == "*":
        result = number1 * number2
        print("Your result is", result)
    elif operator == "/":
        result = number1 / number2
        print("Your result is", result)
    elif operator == "root":
        result = number1 ** number2
        print("Your result is", result)
    elif operator == "^":
        result = number1 ** number2
        print("Your result is", result)
