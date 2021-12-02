from unittest import TestCase


class SharedFixture(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass Shared")

    def setUp(self) -> None:
        print("setUp Shared")

    def tearDown(self) -> None:
        print("tearDown Shared")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass Shared")


def some_great_module_setup_1():
    print("some_great_module_setup 1")


def some_great_module_setup_2():
    print("some_great_module_setup 2")
