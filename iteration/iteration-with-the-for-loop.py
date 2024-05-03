# An object is iterable if it's element can be stepped through one by one
# An iterable object is a data structure from which successive items can be obtained until the supply is exhausted

# dinner = "Steak and Potatoes" 

# for character in dinner:
#     print(character)


numbers = [2, 3, 5, 7, 10]

for number in numbers:  
    print(number * number)

print()
print()

novelists = ["Fitzgerald", "Hemmingway", "Steinbeck"]

for novelist in novelists:
    print(len(novelist))


print(novelist)
print(number)



total = 0

for number in numbers:
    total = total + number
   
print(total)

print()
print()
print()


meals = "rice and beans"

for meal in meals:
    print(meal.title())


print(meal + " " + "Yes")

print()
print()
print()

awon_numbers = [20,45,67,78,78]

sum = 0

for one_number in awon_numbers:
    
    sum = sum + one_number
    
print(sum)