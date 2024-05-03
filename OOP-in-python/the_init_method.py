# The __init__ method will run automatically whenever an object is instantiated from our class

class Guitar():
    def __init__(self):
        print(f"A new guitar is being created! {self}")



bass = Guitar()
acoustic = Guitar()