name = "Boris"
age = 27
handsome = True
favorite_language = "Python"


print(name, age)

name = "Stephen"
print(age + 4)
print("My name is", name, "and I am", age, "years old")

fact_or_fiction = 6 < 10

print(fact_or_fiction)


# Multiple variable assignments
a = b = 5

b = 10

print(a,b)

a, b, c, d= 3,10, 15, 20
print(a)
print(b)
print(c)
print(d)


# Augmented assignment operator
a = 1

# What happens on the right side takes place first  
a = a + 3
print(a)

a = 1 

a += 2
print(a)


word = "race"

word = word + "car"

print(word)


r = 5

r *= 3
print(r)


