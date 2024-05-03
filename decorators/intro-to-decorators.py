# A decorator in Python is an HOF accepts a function as an input and returns a value as an output

def be_nice(fn):
    def inner():
        print("Waiting to execute.....")
        fn()
        print("Execution complete")
    return inner

# Syntactic sugar
@be_nice
def complex_logic():
    print("Execution in progress..........")


@be_nice
def nonsense():
    print("Goo goo gaga..........")

nonsense()
# complex_logic()

# be_nice(complex_logic)()
# result = be_nice(complex_logic)
# result()

