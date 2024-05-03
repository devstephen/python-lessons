# Zero is the only numeric falsy value

if 3: 
    print("Hello")

if -1:
    print("Goodbye")

if 0:
    print("Will this work?")


# An empty string is a falsy value, any other length is a truthy value
if "Hello":
    print("La la la")

if "":
    print("This will not print")
    


print(bool(1))
print(bool(0))
print(bool(""))
print(bool("Hello"))
print(bool(3.22345678))
print(bool(0))

