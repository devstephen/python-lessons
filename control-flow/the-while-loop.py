# A loop is a series of instructions that is repeated 
# A while loop continues to loop while the condition is true
# A infinite loop runs forever

# count = 0

# while count <= 5:
#     print(count)
#     count += 1

# print(count)

# count = 0

# while count <= 5:
#     print(count)
#     count += 1


invalid_number = True

while invalid_number:
    user_value = int(input("Please enter a number above 10: "))
    if user_value > 10:
        print(f"Thanks, that works fine! {user_value} is a great choice")
        invalid_number = False
    else:
        print("That doesn't fit! Try again")
