import collections

Book = collections.namedtuple("Book", [ "title", "author" ])

book1 = Book("Eat That Frog", "Brian Tracy")
gatsby = Book(title="The Great Gatsby", author= "F. Scott")

print(gatsby[0])
print(book1[1])

print(book1.title)
print(book1.author)