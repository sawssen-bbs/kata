import unittest
from strategies.others_strategy import OthersStrategy
from strategies.tens_strategy import TensStrategy
from strategies.units_strategy import UnitStrategy
from tools import file_to_list


class TestOthersStrategy(unittest.TestCase):
    def setUp(self):
        units = file_to_list("../configurations/units.txt")
        tens = file_to_list("../configurations/tens.txt")

        self.units_strategy = UnitStrategy(units)
        self.tens_strategy = TensStrategy(tens)

        self.others_strategy = OthersStrategy(
            self.units_strategy,
            self.tens_strategy
        )

    def test_transform(self):
        # Test cases for the transform method
        test_cases = [
            (17, "dix-sept"),  # 17 -> "dix-sept"
            (22, "vingt-deux"),  # 22 -> "vingt-deux"
            (32, "trente-deux"),  # 32 -> "trente-deux"
            (42, "quarante-deux"),  # 42 -> "quarente-deux"
            (41, "quarante-un"),  # 41 -> "quarente-et-un"
        ]

        for number, expected_result in test_cases:
            with self.subTest(number=number):
                result = self.others_strategy.transform(number)
                self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
