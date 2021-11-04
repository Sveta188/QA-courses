def f(x):
    f = lambda x: x + 100
    return f(x)


print([f(i) for i in range(1, 11)])
