# List comprehension in Python is a concise way to create a new list based on the elements of an existing iterable object

numbers = [3, 4, 5, 6, 7]
# squares = []

# for number in numbers:
#     squares.append(number ** 2)

# print(squares)



squares = [number ** 2 for number in numbers]
print(squares)



rivers = [ "Amazon", "Nile", "Yangtze" ]

rivers_len = [len(river) for river in rivers ]
print(rivers_len)

expressions = [ "lol", "rofl", "lmao"  ]

new_expressions = [expression.upper() for expression in expressions ]
print(new_expressions)

decimals = [ 4.95, 3.28, 1.08 ]

integers = [int(decimal) for decimal in decimals]
print(integers)

whole_numbers = [ 100, 30, 101, 6, 78, 89, 29, 43 ]
print()
print()
print()
floating_numbers = [float(number) for number in whole_numbers]
print(floating_numbers)