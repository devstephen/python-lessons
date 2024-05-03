# A method is a function that acts on a specific object. A method is also a function attached to an object.
# Just like a function, a method needs to be invoked

# A substring is a smaller string that we look for in a larger string

# The find method looks for a substring and returns its index position
# Find method returns -1 if the substring is not found, does not crash


browser = "Google Chrome CCC"

print(browser.find("C"))
print(browser.find("Ch"))
print(browser.find("o"))
print(browser.find("G"))

print("___________________________")
print("___________________________")

print(browser.find("o"))
print(browser.find("o", 2))
print(browser.find("o", 5))

# Boolean value for find
# Use the in operator to check for inclusion, if index does not matter
print("Ch" in browser)

# The index method
# Index method throws an error and crashes the program if the substring is not found
print("___________________________")

print(browser.index("G"))








