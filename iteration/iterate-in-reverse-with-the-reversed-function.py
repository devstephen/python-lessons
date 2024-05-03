# Print an arrays in reverse
the_simpsons = [ "Homer", "Marge", "Bart", "Lisa", "Maggie"]

for character in the_simpsons[::-1]:
    print(f"{character} has a total of {len(character)} characters in their name")


print(type(reversed(the_simpsons)))


for character in reversed(the_simpsons):
    print(f"{character} has a total of {len(character)} characters in their name")
