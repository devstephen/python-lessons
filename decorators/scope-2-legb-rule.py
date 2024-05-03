# LEGB - Local / Enclosing Functions / Global / Built-in
def outer():
    x = 10

    def inner():
        x = 5
        return x
    return inner()

print(outer())