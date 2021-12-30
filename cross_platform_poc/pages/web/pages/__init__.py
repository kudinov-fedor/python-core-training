class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def super(self):
        return type(self).__mro__[1](self.driver)


class LoginPage(BasePage):

    def login(self):
        print(self.driver, self.__class__.__name__, " login")
        return BooksPage(self.driver)


class BooksPage(BasePage):

    def __new__(cls, driver, *args, **kwargs):
        page_class = {
            "safari": BooksPageSafari,
            "chrome": BooksPageChrome
        }.get(driver[0], cls)
        if page_class is not cls and cls in page_class.__mro__:
            return page_class(driver)
        return super().__new__(cls)

    def get_books(self):
        print(self.driver, self.__class__.__name__, " get_books")
        return ["book1", "book2", "book3"]


class BooksPageSafari(BooksPage):

    def get_books(self):
        print(self.driver, self.__class__.__name__, " get_books")
        return ["book1 safari", "book2 safari", "book3 safari"]


class BooksPageChrome(BooksPage):

    def get_books(self):
        print(self.driver, self.__class__.__name__, " get_books")
        return ["book1 chrome", "book2 chrome", "book3 chrome"]


class ProfileBooksPage(BooksPage):

    def add_book(self, index: int):
        books = self.super.get_books()  # get books from correct BooksPage subclass based on driver
        print(self.driver, self.__class__.__name__, " add_book ", books[index])
