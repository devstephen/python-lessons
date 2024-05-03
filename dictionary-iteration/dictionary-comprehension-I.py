languages = [
    "Python", 
    "JavaScript",
    "Ruby"
]


lengths = { language: len(language) for language in languages if "t" in language }
print(lengths)

iterate = {str: "Mementos".count(str) for str in "Mementos" if str > "m" }

print(iterate)