pokemon = {
    "Fire": [ "Charmander", "Charmelon", "Charizard" ],
    "Water": [ "Squirtle", "Warturtle", "Blastoise" ],
    "Grass": [ "Bulbasaur", "Venusaur", "Ivysaur" ]
  
 }

print( "Fire" in pokemon )
print( "Gras" not in pokemon )
print( "Grass" not in pokemon )

if "Zombie" in pokemon: 
    print(pokemon["Zombie"])
else:
    print("The category does not exist")