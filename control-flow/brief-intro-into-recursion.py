# Recursion is when a function calls itself
# Recursion is the invocation of a function from within itself
# def count_down_from(number):
#     start = number
#     while start > 0:
#         print(start)
#         start -= 1

def count_down_from(number):
    if number <= 0:
        return
    
    # Else is not really need
    else:
        print(number)
        count_down_from(number - 1)

count_down_from(5)


# Challenge 2

# def reverse(str):
#     start_index = 0
#     last_index = len(str) - 1 
#     reversed_string = ""

#     while last_index >= start_index:
#         reversed_string += str[last_index]
#         last_index -= 1

#     return reversed_string


def reverse(str):
    # Base case
    if len(str) <= 1:
        return str

    return  str[-1] + reverse(str[0:-1])

print(reverse("bruv"))