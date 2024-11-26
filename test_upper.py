import unittest


class TestStringUpper(unittest.TestCase):
    def test_normal(self):
        self.assertEqual("hello".upper(), "HELLO")


if __name__ == "__main__":
    unittest.main()
