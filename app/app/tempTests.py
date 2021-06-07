from django.test import TestCase


from app.tempCalc import add, subtract


class CalcTests(TestCase):  # CalcTests class inherit from TestCase

    def test_add_numbers(self):
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        self.assertEqual(subtract(5, 11), 6)
