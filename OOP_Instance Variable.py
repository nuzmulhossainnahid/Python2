class StoryBook:
    # Class Variable
    no_of_books = 0

    discount = 0.5

    def __init__(self, name, price, author_name, author_born):
       self.name = name
       self.price = price
       self.author_name = author_name
       self.author_born = author_born
       StoryBook.no_of_books +=1

    # regular method 1
    def get_book_info(self):
        print(f'The book name: {self.name}, price: {self.price}')

    # applying discount
    def appy_discount(self):
        self.price = int(self.price - self.price * self.discount)


book_1 = StoryBook('Nahid', 120, 'Hasan', 1546)
book_2 = StoryBook('Zahid', 130, 'Kabir', 1652)
book_2.author_name = 'FFFf'

book_1.get_book_info()
StoryBook.get_book_info(book_2)

print(book_2.price)
book_2.discount = 0.3
book_2.appy_discount()
print(book_2.price)



