sport_team_rosters =  {
    "New England Patriots": [ "Tom Brady", "Rob Gronkowski", "Julian Edelman" ],
    "New York Giants": [ "Eli Manning", "Odell Beckham " ]
}

sport_team_rosters["Pittsburgh Steelers"] = [ "Ben Roeth", "Antonio Brown" ]

sport_team_rosters["New York Giants"] = [ "Eli Manning" ]
print(sport_team_rosters["New York Giants"])

video_game_options  = {  }


video_game_options["subtitles"] = True
video_game_options["difficulty" ] = "Medium"
video_game_options["volume"] = 7

print(video_game_options)

video_game_options["volume"] = 50
video_game_options["subtitles"] = False
print(video_game_options)


words = [ "danger", "beware", "danger", "beware", "beware" ]

def count_words(words):
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

print(count_words(words))