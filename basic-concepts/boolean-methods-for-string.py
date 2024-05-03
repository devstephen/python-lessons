# Check for lower case only strings regardless of other characters
print("winter".islower())
print("winter  345678".islower())
print("winteR  345678".islower())

print("___________________________")

# Check for upper case only strings regardless of other characters in the string
print("WINTER  345678".isupper())
print("WINTER  3r45678".isupper())


print("___________________________")

# Check for title case only strings regardless of other characters in the string
print("The 4 Seasons".istitle())


print("___________________________")

# Check for alphabets only strings and mindful of other characters in the string
print("WINTER".isalpha())


print("___________________________")

# Check for alphanumeric only strings regardless of other characters in the string
print("WINTER34567890 ".isalnum())

print("___________________________")
# Check for strings with space ony
print(" ".isspace())
