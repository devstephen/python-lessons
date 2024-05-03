def length(word):
    return (len(word))

# print(length("Hello"))
# print(length( word = "Hello"))


def collect_keyword_arguments(**kwargs):
    print(kwargs)
    print(type(kwargs))

    for key, value in kwargs.items():
        print(f" The key is {key} and the value is {value} ")

collect_keyword_arguments(a =2, b = 3, c = 4, d = 5, f= 6)

def args_and_kwargs(a, b, c, *args, **kwargs):
    print(f"The total of your regular arguments is {a + b}")
    print(f"The total of your args tuple is {sum(args)}")
    print(f"The total of your args tuple is {sum(args)}")


args_and_kwargs(1,2,3,4,5,6,7)