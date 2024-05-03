# Add  only odd numbers
values = [3, 6, 9, 12, 15, 18, 21, 24 ]
other_values = [ 5, 10, 15, 20, 25, 30] 

def odds_sum(numbers):
    total = 0
    for number in numbers:
        if number % 2 == 1:
            total = total + number
    return total


print(odds_sum(values))
print(odds_sum(other_values))


# Find the greatest number 
def greatest_number(numbers):
    greatest = numbers[0]
    for number in numbers:
        if number > greatest:
            greatest = number
    return greatest


print(greatest_number([300, 10, 200, 7, 2000]))
print(greatest_number(["Ssahm", "Quinn", "Testerbird"]))
