# The __init__ method will run automatically whenever an object is instantiated from our class

class Guitar():
    def __init__(self):
        print(f"A new guitar is being created! {self}")

# An attribute is a piece of data stored on an object
# Attributes are public by default and can be accessed with dot syntax

electric = Guitar()
acoustic = Guitar()

acoustic.wood = "Mahogany"
acoustic.strings = 6
acoustic.year = 1990

electric.nickname = "Sound Viking 3000"

print(acoustic.wood)
print(electric.nickname)