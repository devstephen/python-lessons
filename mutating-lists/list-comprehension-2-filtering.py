print(["abcdefghijklmnopqrstuvwxyz".index(char) for char in "donut"
    ])

divide_by_2 = [int(number / 2) for number in range(20)]
print(divide_by_2)

donuts = [
    "Boston Cream",
    "Jelly",
    "Vanilla Cream",
    "Glazed",
    "Chocolate Cream"
]

# creamy_donuts = []

# for donut in donuts:
#     if "Cream" in donut:
#         creamy_donuts.append(donut)
    

# print(creamy_donuts)

creamy_donuts = [donut for donut in donuts if "Cream" in donut]
print(creamy_donuts)

print([len(donut) for donut in donuts if "Cream" in donut])
print([donut.split(" ")[0] for donut in donuts if "Cream" in donut])