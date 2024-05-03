# The extend method adds a list of elements to the end of an array
# It takes the elements of a new array and extend it to the list the method is applied on 

mountains = ["Everest", "K2"]
print(mountains)

mountains.extend(["K3", "K4", "Olive"])
print(mountains)

extra_moutains = ["Cho Oyu", "Dhaulagiri"]
mountains.extend(extra_moutains)
print(mountains)


steaks = ["Tenderloin", "New York Strip"]
more_steaks = ["T-Bone", "Ribeye"]

# The original list are not modified
my_meal = steaks + more_steaks
print(my_meal)

# Here is how to modify the original lists

steaks = steaks + more_steaks