name = input("Enter a name: ").strip()
adjective = input("Enter an adjective ").strip()
noun = input("Enter a noun ").strip()

# letter before quotes is case insensitive and it must be an f/F
mad_libs = f"{name} laughed at the {adjective} {noun}."

print(mad_libs)

print(f"2 + 2 is {2 + 2} ")