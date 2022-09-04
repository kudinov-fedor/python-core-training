from unittest import TestCase
from unittest.mock import patch


class Calculator:
    def sum(self, a, b):
        return a + b

    def __divmod__(self, a, b):
        return divmod(a,b)


class TestCalculator(TestCase):
    #@patch('main.Calculator.sum', return_value=2)     #doesn't work..
    def setUp(self) -> None:
        self.calc = Calculator()


    def test_sum(self):
        answer = self.calc.sum(2, 4)
        self.assertEqual(answer, 2)

    def test_divmod(self):
        answer = self.calc.__divmod__(5,3)
        self.assertEqual(answer, (1,2))