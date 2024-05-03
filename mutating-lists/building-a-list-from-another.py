powerball = [4, 8, 15, 16, 23, 42]

def squares(numbers):
    squares = []

    for number in numbers:
        squares.append(number ** 2)
    return squares

    
    

print(squares(powerball))




def convert_to_floats(numbers):
    floating_number = []

    for number in numbers:
        floating_number.append(float(number))

    return floating_number

print(convert_to_floats(powerball))
print(convert_to_floats([20.1, 10, 101]))

def even_or_odd(numbers):
    booleans = []

    for number in numbers:
        if number % 2 == 0:
            booleans.append(True)
        else:
            booleans.append(False)
    return booleans


print(even_or_odd(powerball))