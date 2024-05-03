
def add(x, y):
    # Assertion is a validation of a condition being met
    assert isinstance(x, int) and isinstance(y, int), "Both arguments must be integers"
    return x + y    


print(add("3", 6)) 