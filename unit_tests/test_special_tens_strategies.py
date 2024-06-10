import unittest
from strategies.special_tens_strategy import SpecialTenStrategy
from strategies.tens_strategy import TensStrategy
from strategies.units_strategy import UnitStrategy
from strategies.others_strategy import OthersStrategy
from tools import file_to_list


class TestSpecialTenStrategy(unittest.TestCase):
    def setUp(self):

        units = file_to_list("../configurations/units.txt")
        tens = file_to_list("../configurations/tens.txt")

        self.units_strategy = UnitStrategy(units)
        self.tens_strategy = TensStrategy(tens)
        self.other_strategy = OthersStrategy(self.units_strategy, self.tens_strategy)

        self.special_tens_strategy = SpecialTenStrategy(self.units_strategy, self.tens_strategy, self.other_strategy)

    def test_transform(self):
        test_cases = [
            (70, "soixante-dix"),
            (71, "soixante-et-onze"),
            (76, "soixante-seize"),
            (80, "quatre-vingt"),
            (81, "quatre-vingt-un"),
            (86, "quatre-vingt-six"),
            (90, "quatre-vingt-dix"),
            (96, "quatre-vingt-seize"),
            (98, "quatre-vingt-dix-huit"),
        ]

        for number, expected_result in test_cases:
            with self.subTest(number=number):
                result = self.special_tens_strategy.transform(number)
                self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
