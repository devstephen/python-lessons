employee = ( "Bob", "Johnson", "Manager", 50 )

first_name, last_name, *details = employee
print(first_name, last_name, details)

*names, position, age = employee
print(names, position,  age)


first, *last_title, age = employee
print(first, last_title, age )


first_name, last_name, position, *details = employee
print(details)