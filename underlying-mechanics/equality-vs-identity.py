students = [ "Bob", "Sally", "Sue" ]
athletes = students
nerds = [ "Bob", "Sally", "Sue" ]

print(students == athletes)
print(students == nerds)

print(students is athletes)
print(students is nerds)

a = 1
b = 1

print( a is b)
print( a == b)