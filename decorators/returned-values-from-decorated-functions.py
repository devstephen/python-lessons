# A decorator in Python is an HOF accepts a function as an input and returns a value as an output

def be_nice(fn):
    def inner(*args, **kwargs):
        print("Waiting to execute.....")
        result =  fn(*args, **kwargs)
        print("Execution complete")
        return result
    return inner

# Syntactic sugar
@be_nice
def complex_logic_sum(a, b):
    return a + b

print(complex_logic_sum(a = 3, b = 3))





