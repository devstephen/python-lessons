import collections

Book = collections.namedtuple("Book", [ "title", "author" ])

book1 = Book("Eat That Frog", "Brian Tracy")
gatsby = Book(title="The Great Gatsby", author= "F. Scott")

word = "dynasty"

# print(len(word))
# print(word.__len__())


class Library():
    def __init__(self, *books):
        self.books = books       
        self.librarians = []

    def __len__(self):
        return len(self.books)
    

l1 = Library(book1)
l2 = Library(book1, gatsby)

print(len(l1))
print(len(l2))