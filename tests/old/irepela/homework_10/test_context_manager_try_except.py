from irepela.homework_10.context_manager_try_except import Catcher


def test_try_except():
    with Catcher():
        5 / 0

    with Catcher(ZeroDivisionError):
        5 / 0

    with Catcher(TypeError, ZeroDivisionError):
        5 / 0

    with Catcher(None):
        5 / 5
