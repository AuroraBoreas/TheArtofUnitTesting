import random

def f(arg):
    return arg * random.randint(1, 100)

def g(a: int):
    return f(a) ** 2