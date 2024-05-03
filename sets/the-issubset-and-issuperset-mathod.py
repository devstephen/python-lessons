a = { 1, 2, 3 }
b = { 1, 2, 3, 4, 5 }

print(a.issubset(b))
print(a <= b)

print()
print(b.issubset(a))
print()
print(b.issuperset(a))
print(b >= a)
