def func(arr: list) -> map:
    return [val for val in filter(lambda x: x % 2 != 0, arr)]


print(func([x for x in range(1, 11)]))
