# The append method adds an element to the end of a list
countries = ["United States", "Canada", "Australia"]
print(countries)
print(len(countries))


# The original list has been mutated not that a new list has been created

print(countries)
print(len(countries))


# No need to do this
countries = countries.append("France")
print(countries)
