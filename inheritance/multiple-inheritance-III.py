class FilmMaker():
    def give_interview(self):
        print("I love making movies")


class Director(FilmMaker):
    pass

class ScreenWriter(FilmMaker):
    def give_interview(self):
        print("I love writing scripts")

class JackOfAllTrades(ScreenWriter, Director):
    pass

print(JackOfAllTrades.mro())

stallone = JackOfAllTrades()
stallone.give_interview()