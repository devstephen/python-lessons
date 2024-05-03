import time


class Garbage():
    """""
    Deletes an object when reference is no longer being made to it in a program
    """

    def __del__(self):
        print("Final call to delete!")


g = Garbage()

g = [ 1,2 ,3]

time.sleep(5)

print("Program ended")