empty_space = "            content       "

# Remove spaces on the right side of the string
print(len(empty_space))
print(empty_space.rstrip())
print(len(empty_space.rstrip()))

print()
print()

# Remove spaces on the left side of the string
print(empty_space.lstrip())
print(len(empty_space.lstrip()))


# Remove spaces on the both sides of the string
# The strip method removes characters at the beginning and end of a string
# The character in the middle are ignored
# You can pass an optional argument of characters you want to remove
# If you don't feed it any argument, it will default to removing spaces on the left and right sides
print(empty_space.strip())
print(len(empty_space.strip()))


# The strip method removes characters at the beginning and end of a string
# The character in the middle are ignored
# You can pass an optional argument of characters you want to remove
website = "www.python.org"
print(website.lstrip("w."))
print(website.rstrip("org"))
print(website.strip("w.org"))