# Short circuit evaluation also applies here
if 5 > 8 or 7 < 11:
    print("At least one is true")


if "cat" == "cat" or "dog" == "donkey":
    print("At least one is true")


if "cat" == "cat" or "dog" == "dog":
    print("Will this print? Yes!")

if "apple" == "banana" or "orange" == "pear":
    print("Will this print? Nope!")