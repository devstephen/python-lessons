# Scope refers to the locations in a program in which a name (variable, functions) can be used
# A shadow variable is a local variable tha shares the same name as a global variable
# A constant is a name that does not change over the program's execution
age = 28

def fancy_func():
    age = 100
    print(age)    

fancy_func()
print(age)

TAX_RATE = 0.06


def calculate_tax(price):
    return round(price * TAX_RATE, 2)

print(calculate_tax(23.99))


def calculate_tip(price):
    return round(price * (TAX_RATE * 3), 2)

print(calculate_tip(10))