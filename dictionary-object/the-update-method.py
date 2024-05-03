employees_salaries = {
  "Guido": 100000,
  "James": 500000,
  "Brandon": 900000
  }


extra_employees_salaries = {
    "Yuki": 1000000,
    "Guido": 333333
}

# Merge two dictionaries 

# employees_salaries.update(extra_employees_salaries)
extra_employees_salaries.update(employees_salaries)

print(extra_employees_salaries)

# print(employees_salaries)
