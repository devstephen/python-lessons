print(type({"a":1}))

print(isinstance(1, int))
print(isinstance({}, dict))
print(isinstance([], list))
print(isinstance([], int))

print(isinstance(1, object))
print(isinstance(1, object))
print(isinstance(1, object))
print(isinstance(str, object))


class Person():
    pass

class Superhero(Person):
    pass


print()
print()
arnold = Person()
boris = Superhero()

print(isinstance(boris, Superhero))
print(isinstance(boris, Person))
print(isinstance(arnold, Person))
print(isinstance(arnold, Superhero))

print()
print("Ehen")
print(issubclass(Superhero, Person))
print(issubclass(Person, Superhero))
print(issubclass(Superhero, object))
print(issubclass(Person, object))