# The remove method removes an element based on a given value, not it's index position
# If the element is recurrent, it will remove the first occurence of the element
nintendo_games = ["Zelda", "Donkey Kong", "Mario", "Zelda"]

nintendo_games.remove("Zelda")
nintendo_games.remove("Zelda")
print(nintendo_games)

if "Luigi" in nintendo_games:
    nintendo_games.remove("Luigi")


if "Mario" in nintendo_games:
    nintendo_games.remove("Mario")

print(nintendo_games)
