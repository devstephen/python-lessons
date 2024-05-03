# x = 10 


def change_stuff():
    global x
    # The local x variable in this function is tossed out of memory after the invocation 
    x = 15

# print(x)
change_stuff()
print(x)