from cross_platform_poc import pages


def test_books(driver):
    books_page = pages.LoginPage(driver).login()
    books = books_page.get_books()
    assert len(books) == 3
    print(books)


def test_books_2(driver):
    book = pages.ProfileBooksPage(driver).add_book(1)
    print(book)
