from unittest import TestCase, mock, skip
import math
from parameterized import parameterized

from . import module_with_random
from .shared_fixtures import SharedFixture, some_great_module_setup_1, some_great_module_setup_2
from .module_with_random import my_func_returns_random, ClassWithConnection


def setUpModule():
    print("setUpModule")
    some_great_module_setup_1()
    some_great_module_setup_2()


def tearDownModule():
    print("tearDownModule")


class TestMyTests1(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass 1")

    def setUp(self) -> None:
        print("setUp 1")

    def tearDown(self) -> None:
        print("tearDown 1")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass 1")

    # -------------------------------

    def test_demo_success(self):
        assert 1 == 1

    def test_demo_failure(self):
        self.assertEqual(1,  2, "some smart message")

    def test_assert_rasise(self):

        with self.assertRaises(ZeroDivisionError):
            10/0

    @parameterized.expand([
       (-1.5, -2.0),
       (1, 1.0),
       (1.6, 1),
    ])
    def test_floor(self, input, expected):
        self.assertEqual(math.floor(input), expected)

    @mock.patch("tests.unittest_example.module_with_random.random")
    def test_mock(self, rand_mock):
        rand_mock.return_value = 10.0
        self.assertEqual(my_func_returns_random(), 10.0)

    def test_mock_object(self):
        with mock.patch.object(module_with_random, "random") as rand_mock:
            rand_mock.return_value = 10.0
            self.assertEqual(my_func_returns_random(), 10.0)

    def test_monkey_patch_class(self):

        with mock.patch.object(ClassWithConnection, "connect"):
            connector = ClassWithConnection("10.0.0.123:8888")
            # do smth with connector

            self.assertTrue(ClassWithConnection.connect.called)

    @skip("do not want to run it")
    def test_skip(self):
        raise AssertionError


class TestMyTests2(SharedFixture):

    def test_demo_2(self):
        assert 1 == 1
