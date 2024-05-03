# Shared references means two variables that reference the same object

a = 3
b = a

a = 5
print(a)
print(b)

a = [1, 2, 3, 4]
b = a

a.append(5)
print(a)
print(b)