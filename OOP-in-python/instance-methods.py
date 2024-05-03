# Instance Method can be viewed as a function that belongs to an object

class Pokemon():
    def __init__(self, name, specialty, health = 100) -> None:
        self.name = name
        self.specialty = specialty
        self.health = health


    def roar(self):
        print("Raaaaaaarrrrr")


    def describe(self):
        print(f"I am {self.name}. I am a {self.specialty} Pokemon")

    def take_damage(self, amount):
        self.health -= amount

squirtle = Pokemon("Squirtle", "Water")
charmander = Pokemon(name = "Charmander", specialty = "Fire", health = 101)

squirtle.describe()
charmander.describe()
squirtle.take_damage(20)
print(squirtle.health)