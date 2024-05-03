class Restaurant():
    def make_reservation(self, party_size):
        print(f"Booked a table for {party_size}")


class SteakHouse(Restaurant):
    pass


class Bar():
    def make_reservation(self, party_size):
        print(f"Booked a lounge for {party_size}")

class BarAndGrill(SteakHouse, Bar):
    pass


bag = BarAndGrill()
# Depth first searchs
bag.make_reservation(2)