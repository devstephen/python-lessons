# A decorator in Python is an HOF accepts a function as an input and returns a value as an output

def be_nice(fn):
    def inner(*args, **kwargs):
        print("Waiting to execute.....")
        fn(*args, **kwargs)
        # print(args)
        # print(kwargs)
        print("Execution complete")
    return inner

# Syntactic sugar
@be_nice
def complex_logic(stakeholder, hello):
    print(f"Something complex for {hello} {stakeholder}")

complex_logic(stakeholder= "Boris", hello = "CEO")
complex_logic("Boris", "CEO")




