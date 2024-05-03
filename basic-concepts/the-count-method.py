# The count methods returns an integer that represents the number of times a substring occurs on a string
# The method returns zero when substring is non-existent
# Queueing is the only word in english that has five vowels in a row

word = "queueing"

print(word.count("u"))
print(word.count("e"))
print(word.count("Q"))
print(word.count("ue"))
print(word.count("ing"))

# Sum of two substrings
print(word.count("u") + word.count("e"))
