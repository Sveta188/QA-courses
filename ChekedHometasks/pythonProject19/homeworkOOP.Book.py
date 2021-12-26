"""1.1 Создайте класс book с именем книги, автором, кол-м страниц, флагом, зарезервирована ли книги или нет."""


class Book:
    def __init__(self, book):
        self.name = book[0]
        self.author = book[1]
        self.pages = book[2]
        self.booked = book[3]
        self.taken = book[4]

    def library(self):
        print(self.name, self.author, self.pages, self.booked, self.taken)


"""1.2 Создайте класс пользователь который может брать книгу, возвращать, бронировать.
Если другой пользователь хочет взять зарезервированную книгу(или которую уже кто-то читает - надо ему про это сказать)."""


class Person(Book):
    def __init__(self, book):
        super().__init__(book)

    def take_a_book(self, book):
        if self.taken:
            print("Book is taken by reader")
        else:
            self.taken = True
            print("Book is taken")

    def return_a_book(self, book):
        if self.taken:
            self.taken = False
            print("Book is returned")
        else:
            print("You can't returned a book, which you're not taken")

    def __booked__(self, book):
        if self.booked:
            print("Book is reserved by other reader")
        else:
            self.booked = True
            print("Book is reserved")


book_1 = ['Book1', 'Author', 4567, False, False]
book_2 = ['Book2', 'Author', 4567, True, True]

book1 = Person(book_1)
book2 = Person(book_2)
book1.library()
book2.library()
book1.take_a_book(book1)
book1.return_a_book(book1)
book2.take_a_book(book2)
book1.__booked__(book1)
book2.__booked__(book2)
