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


class Calculator:

    def operations(self):
        print("'+...Addition")
        print("- ... Subtraction")
        print("*... Multiplication")
        print("/ ...Division")
        print("root...Root, please enter the second number in fractional format")
        print("^...Square")

    def input_operator(self):
        print(Color.BOLD + "The list of abilities for calculator" + Color.END)
        while True:
            operator = input("Enter the operator, if you want to see all offered operations - type help"
                             "If you want to exit- type exit:")
            if operator == "help":
                self.operations()
            elif operator == "exit":
                sys.exit()
            elif operator == "+" or operator == "/" or operator == "-" or operator == "*" or operator == "root" or operator == "^":
                return operator
            else:
                print("Error, try again")

    def input_numbers(self, text):
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

    def input_first_number(self,text):
        return self.input_numbers("Enter the first number")

    def input_second_number(self, text, operator):
        while True:
            number2 = self.input_numbers(text)
            if operator == "/" and number2 == 0:
                print("Error! You try to divide on 0")
            else:
                return number2

    def process_numbers(self, number1, number2, operator):
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
            result = number1 ** (1 / number2)
            print('Your result is', result)
        elif operator == "^":
            result = number1 ** number2
            print('Your result is', result)

    def calculate(self):
        while True:
            operator = self.input_operator()
            number1 = self.input_first_number('Enter the first number')
            number2 = self.input_second_number('Enter the second number', operator)
            self.process_numbers(number1, number2, operator)


Calculator().calculate()
