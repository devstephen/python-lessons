# with open("cupcake.txt", "r") as cupcakes_file:
#     print("The file has been opened!")
#     content = cupcakes_file.read()
#     print(content)

# print("The file has been closed. We're now outside the execution context")


filename = input("What file would you like to open?  ")
with open(filename, "r") as cupcake_file:
    print("File has been opened!")
    content = cupcake_file.read()
    print(content)
    print()
print("File is now closed! We are now outside the execution context.")