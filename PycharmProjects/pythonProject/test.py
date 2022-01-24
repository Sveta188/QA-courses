import unittest

from func import Calculator


class MiTest(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
    def test_add(self):
        self.assertEqual(self.calculator.add(4,7), 11)


