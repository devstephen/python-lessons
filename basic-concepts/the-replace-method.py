# The replace method find a substring in a string and replaces it with a provided string
# It works exactly the same way find and replace does in a word processing software
# The first argument is the character(s) be replaced and the second is the replacement

phone_number = "555 555 1234"
print(phone_number.replace(" ", "-"))
print(phone_number.replace("5", "9"))

phone_number = phone_number.replace(" ", "-")
print(phone_number)