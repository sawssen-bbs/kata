import unittest
from strategies.units_strategy import UnitStrategy
from tools import file_to_list


class TestUnitStrategy(unittest.TestCase):
    def setUp(self):
        units = file_to_list("../configurations/units.txt")
        self.units_strategy = UnitStrategy(units)

    def test_transform(self):
        test_cases = [
            (0, "zéro"),
            (1, "un"),
            (10, "dix"),
            (16, "seize"),
        ]

        for number, expected_result in test_cases:
            with self.subTest(number=number):
                result = self.units_strategy.transform(number)
                self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
