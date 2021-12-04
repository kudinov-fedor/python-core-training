from automationpractice import MainPage


def test_main(session):
    main = MainPage(session).open_page()
    main.search_query_top.send_keys("Hi there")
    main.search_query_top.submit()
