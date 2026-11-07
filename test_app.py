
import unittest
from app import add


class TestApp(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(10, 20), 30)

    def test_zero(self):
        self.assertEqual(add(5, 0), 5)

    def test_negative(self):
        self.assertEqual(add(-5, 5), 0)


if __name__ == "__main__":
    unittest.main()
