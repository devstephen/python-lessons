film_directors = {
    "The Godfather": "Francis Ford Coppola",
    "The Rock": "Michael Bay",
    "Goodfellas": "Martin Scorsese"
}

film_directors.get("Goodfellas")
film_directors.get("Bad Boys", "Michaeal Bay" )

film_directors.setdefault("Men in Black")
film_directors.setdefault("Bad Boys", "Michaeal Bay")
print(film_directors)