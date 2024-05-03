chinese_food = {
    "Sesame Chicken": 9.99,
    "Boneless Spare Ribs": 7.99,
    "Fried Rice": 1.99
}

# This syntax is considered an anti-pattern
# An anti-pattern is a solution to a programming problem that is considered ineffective or counter-productive

# for food in chinese_food:
    # print(f" The food is {food} and the price is {chinese_food[food]} ")



pounds_to_kg = {
    5: 2.26796,
    10:  4.53592,
    25: 11.3398
}

for pound in pounds_to_kg:
    print(f" {pound} pounds is equal to {pounds_to_kg[pound]} kilogram ")