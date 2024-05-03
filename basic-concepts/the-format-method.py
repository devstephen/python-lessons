# name, adjective, noun
mad_libs =  "{} laughed at the {} {}."

print(mad_libs.format("Bobby", "green", "alien"))
print(mad_libs.format("Jennifer", "silly", "tomato"))


mad_libs =  "{2} laughed at the {1} {0}."

print(mad_libs.format("Bobby", "green", "alien"))
print(mad_libs.format("Jennifer", "silly", "tomato"))

print("________________________________")

mad_libs =  "{name} laughed at the {adjective} {noun}."

name = input("Enter a name ")
adjective = input("Enter an adjective ")
noun = input("Enter an noun  ")

print(mad_libs.format(name = name, adjective = adjective, noun = noun))

# print(mad_libs.format(name = "Bobby", adjective = "green", noun =  "alien"))
# print(mad_libs.format(adjective =  "silly", noun =  "tomato", name = "Jennifer"))