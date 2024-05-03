class Mistake(Exception):
    pass

class StupidMistake(Mistake):
    pass

class SillyMistake(Mistake):
    pass


try:
    raise StupidMistake("Just a mistake")
except StupidMistake as e:
    print(f"Caught the error {e}")

try:
    raise StupidMistake("extra mistake")
except Mistake as e:
    print(f"Caught the error {e}")

try:
    raise SillyMistake("extra mistake")
except Mistake as e:
    print(f"Caught the error {e}")    
