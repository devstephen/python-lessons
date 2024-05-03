agents = {
    "Mulder",
    "Scully",
    "Doggett",
    "Reyes"
}

# The remove method raises an error when the key passed in does not exist
# agents.remove("Doggett")
# print(agents)

# The discard method will fail silently (no error raised)
agents.discard("Scully")
print(agents)