# The break keyword terminates a for loop before it reaches it's natural conclusion

def contains(values, target):
    found = False
    for value in values:
        print(value)
        if value == target:
            found = True
            break
    return found

print(contains([1, 2, 3, 4, 5], 3))
