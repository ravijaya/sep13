import unittest
from myutils.utils import power


class DummyTestCase(unittest.TestCase):
    """test case"""

    def test_success(self):
        self.assertEqual(1, 1)

    def test_failure(self):
        self.assertNotEqual(1, 0)


class AlphaMyUtilsTestCase(unittest.TestCase):
    def test_power(self):
        self.assertEqual(8, power(2, 3))

    def test_power_s(self):
        self.assertEqual((8, 4, 8), power(2, 3))


if __name__ == '__main__':
    unittest.main()
