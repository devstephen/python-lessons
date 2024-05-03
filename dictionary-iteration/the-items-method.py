college_courses = {
    "History": "Mr. Washington",
    "Math": "Mr. Newton",
    "Science": "Mr. Einstein"
}


for course, tutor in college_courses.items():
    print(f"{course} is being taught by {tutor}")

for _, professor in college_courses.items():
    print(f"The next professor is {professor}")

# print(college_courses.items())