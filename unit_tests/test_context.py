import unittest
from tools import file_to_list, detect_initial_position, post_cleaning
from context import NumberToWordsContext


class TestNumberToWordsContext(unittest.TestCase):
    def setUp(self):

        units = file_to_list("../configurations/units.txt")
        tens = file_to_list("../configurations/tens.txt")


        self.context = NumberToWordsContext(units, tens)

    def test_transform(self):
        hundredsUpper = file_to_list("../configurations/hundredsUpper.txt", tuple=True)
        test_cases = [
            (10, "dix"),
            (20, "vingt"),
            (30, "trente"),
            (40, "quarante"),
            (0, "zéro"),
            (1, "un"),
            (10, "dix"),
            (16, "seize"),
            (17, "dix-sept"),
            (22, "vingt-deux"),
            (32, "trente-deux"),
            (31, "trente-et-un"),
            (42, "quarante-deux"),
            (41, "quarante-et-un"),
            (70, "soixante-dix"),
            (71, "soixante-et-onze"),
            (76, "soixante-seize"),
            (80, "quatre-vingts"),
            (81, "quatre-vingt-un"),
            (86, "quatre-vingt-six"),
            (90, "quatre-vingt-dix"),
            (96, "quatre-vingt-seize"),
            (98, "quatre-vingt-dix-huit"),
            (109, "cent-neuf"),
            (999, "neuf-cent-quatre-vingt-dix-neuf"),
            (900, "neuf-cents"),
            (100, "cent"),
            (1000000, "un-million"),
            (1000000000, "un-milliard"),
            (2000000000, "deux-milliards"),
            (1000, "mille"),
            (4000, "quatre-milles"),
            (40001, "quarante-mille-un"),
            (-300, "moins-trois-cents"),
            (25000, "vingt-cinq-milles")
        ]

        for number, expected_result in test_cases:
            with self.subTest(number=number):
                maximum_length = 12
                pos = detect_initial_position(number, hundredsUpper, maximum_length)
                result = self.context.transform(number, pos, hundredsUpper, maximum_length)

                self.assertEqual(post_cleaning(result, hundredsUpper), expected_result)



if __name__ == '__main__':
    unittest.main()
