import sys

print(sys.argv)
print(type(sys.argv))

word_length = 0


for arg in sys.argv[1:]:
    word_length = word_length + len(arg)

print(f"The lenght of the command line arguments is {word_length}")

