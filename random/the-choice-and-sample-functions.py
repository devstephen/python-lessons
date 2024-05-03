import random

# The choice function returns a random element from an iterable object

print(random.choice([ "Bob", "Moe", "Curly" ]))
print(random.choice((1, 2, 3)))
print(random.choice("Elephant"))

# The choice function returns a list of values
lottery_numbers = [random.randint(1, 50) for value in range(50)  ]
print(random.sample(lottery_numbers, 10))