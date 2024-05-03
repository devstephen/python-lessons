# Strings are immutable, using methods on them returns a new copy. The original string is not changed
story = "once upon a time"

# Capitalizes the first word in a sentence
print(story.capitalize())

# Capitalizes the first letter of each word in a sentence
print(story.title())

# Capitalizes all letters in a sentence
print(story.upper())

# Makes all letters in a sentence lowercase
print("ONCE UPON A TIME".lower())

# Returns a new string with inverted capitalization
print("Once Upon A Time".swapcase())

# Method chaining
print("BENJAMIN FRANKLIN".lower().title())

# Change the original string to a new one: Reassign
story = story.title()

print(story)