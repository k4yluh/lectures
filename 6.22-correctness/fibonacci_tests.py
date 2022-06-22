import unittest
import fibonacci as fib


class TestFibonacci(unittest.TestCase):
    # NOTE: This test alone is not enough to conclude correctness: a function
    #       that simply *always* returned 0 would pass this test...
    def test01(self):
        self.assertEqual(fib.fibonacci(0), 0)

    def test02(self):
        self.assertEqual(fib.fibonacci(1), 1)

    # NOTE: The above tests do not test the recursive case, and thus do not
    #       have 100% coverage.
    def test03(self):
        self.assertEqual(fib.fibonacci(3), 2)


if __name__ == "__main__":
    unittest.main()
