bubble_tea_flavors = [
    ["Honeydew", "Mango", "Passion Fruit"],
    ["Peach", "Plum", "Strawberry", "Taro"],
    ["Kiwi", "Chocolate"]
]

# print(len(bubble_tea_flavors))
# print(bubble_tea_flavors[0])
print(bubble_tea_flavors[1][2])
print(bubble_tea_flavors[2][1])

print()

for tea in bubble_tea_flavors[0]:
    print(tea)

all_flavors = []

for flavor in bubble_tea_flavors[1]:
    all_flavors.append(flavor)

print()
print()
print(all_flavors)

more_flavors = []

for flavor_pack in bubble_tea_flavors:
    for flavor in flavor_pack:
        more_flavors.append(flavor)


print(more_flavors)


