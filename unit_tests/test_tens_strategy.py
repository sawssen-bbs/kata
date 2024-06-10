import unittest
from strategies.tens_strategy import TensStrategy
from tools import file_to_list


class TestTensStrategy(unittest.TestCase):
    def setUp(self):
        tens = file_to_list("../configurations/tens.txt")
        self.tens_strategy = TensStrategy(tens)

    def test_transform(self):
        test_cases = [
            (10, "dix"),
            (20, "vingt"),
            (30, "trente"),
            (40, "quarante"),
        ]

        for number, expected_result in test_cases:
            with self.subTest(number=number):
                result = self.tens_strategy.transform(number)
                self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
