# Closure is a programming in which a scope retains access to an enclosing scope's names

def outer():
    candy = "Snickers"

    def inner():
        return candy
    
    return inner

the_func = outer()
print(the_func())