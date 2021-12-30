
class BasePage:
    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):

    def login(self):
        print(self.driver, self.__class__.__name__, " login mobile")
        return BooksPage(self.driver)


class BooksPage(BasePage):

    def get_books(self):
        print(self.driver, self.__class__.__name__, " get_books mobile")
        return ["book1", "book2", "book3"]


class ProfileBooksPage(BooksPage):

    def add_book(self, index: int):
        books = self.get_books()  # get books from correct BooksPage subclass based on driver
        print(self.driver, self.__class__.__name__, " add_book mobile", books[index])
