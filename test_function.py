import unittest
from function import add


class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(2, 2), 4)
        self.assertEqual(add(-2, 2), 0)


if __name__ == "__main__":
    unittest.main()
