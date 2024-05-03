# The __init__ method will run automatically whenever an object is instantiated from our class

class Guitar():
    def __init__(self, wood):
        self.wood = wood
        

# An attribute is a piece of data stored on an object
# Attributes are public by default and can be accessed with dot syntax

acoustic = Guitar("Alder")
electric = Guitar("Mahogany")
baritone = Guitar("Alder")

print(acoustic.wood)
print(electric.wood)