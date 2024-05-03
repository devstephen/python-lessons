class FrozenFood():
    def thaw(self, minutes):
        print(f"Thawing in {minutes} minutes ")

    def store(self):
        print("Putting in the freezer")

class Dessert():
    def ad_weight(self):
        print("Putting on the pounds")

    def store(self):
        print("Putting on dessert!!!!!!!!")

class IceCream(Dessert, FrozenFood):
    pass


ic = IceCream()
ic.ad_weight()
ic.thaw(5)
ic.store()

# MRO - Method Resolution Order

print(IceCream.mro())