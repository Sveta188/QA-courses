import math
import random
import sys


class Calculator:
    # empty constructor
    def __init__(self):
        pass

    # add method - given two numbers, return the addition
    def add(self, x1, x2):
        print(x1 + x2)

    # multiply method - given two numbers, return the
    # multiplication of the two
    def multiply(self, x1, x2):
        return x1 * x2

    # subtract method - given two numbers, return the value
    # of first value minus the second
    def subtract(self, x1, x2):
        return x1 - x2

    # divide method - given two numbers, return the value
    # of first value divided by the second
    def divide(self, x1, x2):
        if x2 != 0:
            return x1 / x2


if __name__ == "__main__":
    calculate_1 = Calculator().add(4, 7)
