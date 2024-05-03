errands = ["Go to gym", "Grab lunch", "Get promoted at work", "Sleep"]

# Generate object
print(enumerate(errands))

for index, errand in enumerate(errands):
    print(f"{errand} is number {index + 1 } on my todo list")