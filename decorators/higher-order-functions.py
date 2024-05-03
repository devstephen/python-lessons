# A HOF is a function that either accepts a functions as an argument or returns a function as return value

def one():
    return 1

print(type(one))

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def calculator(func, a, b):
    return func(a, b)

print(calculator(add, 2, 4))
print(calculator(subtract, 2, 4))