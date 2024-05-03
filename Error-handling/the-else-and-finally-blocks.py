x = 10

try:
    print( x + 5 )

except NameError:
    print("Some variable is not defined")

else:
    print("This will print if no error in the try")

finally:
    print("This will print regardless of error")