import random


def lottery():

    numbers = list(map(int, input("Enter the all participated numbers through space").split()))
    return random.choice(numbers)


print(lottery())
