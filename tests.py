from funcs import factorial
import unittest


class TestFactorial(unittest.TestCase):
    def test_0(self):
        self.assertEqual(factorial(0), 1)

    def test_1(self):
        self.assertEqual(factorial(1), 1)

    def test_5(self):
        self.assertEqual(factorial(5), 120)

    def test_8(self):
        self.assertEqual(factorial(8), 40320)

    def test_13(self):
        self.assertEqual(factorial(13), 6227020800)


if __name__ == '__main__':
    unittest.main()
