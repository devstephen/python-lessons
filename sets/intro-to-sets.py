# A set is a mutable, unordered data structure that prohibits duplicate values
# Sets can only contain immutable objects

stocks = { "MSFT", "FB", "IBM", "FB" }
print(stocks)

prices = { 1, 2, 3, 4, 5, 3, 4, 2  }
print(prices)

lottery_numbers = { (1,2,3), (4, 5, 6 ),  (1,2,3) }
print(lottery_numbers)

print(len(stocks))
print(len(prices))
print(len(lottery_numbers))

print( "MSFT" in stocks)
print( "IBM" in stocks)

# print(stocks[2])

# for number in prices:
#     print(number)

for numbers in lottery_numbers:
    print(numbers)
    for number in numbers:
        print(number)

squares = { number ** 2 for number in [-5, -4, -3, 3, 4, 5 ] }
print(squares)