# tests/runner.py
import unittest

# import your test modules
from tests.unittest_example import test_simple


# initialize the test suite
loader = unittest.TestLoader()

# add tests to the test suite
suite_1 = unittest.TestSuite()
suite_1.addTests(loader.loadTestsFromTestCase(test_simple.TestMyTests1))

suite_2 = unittest.TestSuite()
suite_2.addTests(loader.loadTestsFromTestCase(test_simple.TestMyTests2))

all_tests = unittest.TestSuite([suite_1, suite_2])


if __name__ == "__main__":
    # initialize a runner, pass it your suite and run it
    runner = unittest.TextTestRunner(verbosity=3)

    import sys
    _, *marks = sys.argv
    marks = marks or ["all_tests"]

    for m in marks:
        result = runner.run(eval(m))
