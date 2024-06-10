from strategies.units_strategy import UnitStrategy
from strategies.tens_strategy import TensStrategy
from strategies.others_strategy import OthersStrategy
from strategies.special_tens_strategy import SpecialTenStrategy


class NumberToWordsContext:
    def __init__(self, units, tens):
        self.units_strategy = UnitStrategy(units)
        self.tens_strategy = TensStrategy(tens)
        self.other_strategy = OthersStrategy(self.units_strategy, self.tens_strategy)
        self.special_tens_strategy = SpecialTenStrategy(self.units_strategy, self.tens_strategy, self.other_strategy)

    def transform(self, number: int, pos, hundredsUpper, maximum_length) -> str:
        result = ""
        if (number < 0):
            result += "moins"
            number = number * -1
        if 0 <= number <= 16:
            return result + self.units_strategy.transform(number)
        elif 70 <= number <= 99:
            return result + self.special_tens_strategy.transform(number)
        elif number % 10 == 0 and number < 70:
            return result + self.tens_strategy.transform(number)
        elif number <= 99:
            return result + self.other_strategy.transform(number)
        elif pos is not None:
            return result + self.transform_hundreds_upper(number, pos, hundredsUpper, maximum_length)
        else:
            max_number = ["9" for i in range(0, maximum_length)]
            return result + f"number out of bounds! maximum number length is {''.join(max_number)}"

    def generate_text_given_position(self, value, units):
        return value if units != "zéro" else ""

    def transform_hundreds_upper(self, number, pos, hundredsUpper, maximum_length):
        minimum_value = 10 ** hundredsUpper[-1][0]
        result = ""
        hundreds = number // (10 ** hundredsUpper[pos][0])
        if pos < len(hundredsUpper) - 1:
            if hundreds != 0:
                text = self.transform(hundreds // minimum_value,
                                      pos, hundredsUpper,
                                      maximum_length)
                result += "-" + self.generate_text_given_position(text + "-" + \
                                                                  hundredsUpper[-1][1],
                                                                  text)

            result += "-" + self.generate_text_given_position(self.transform(hundreds % minimum_value,
                                                                             pos, hundredsUpper,
                                                                             maximum_length) + "-" + \
                                                              hundredsUpper[pos][1],
                                                              self.transform(hundreds % minimum_value,
                                                                             pos, hundredsUpper,
                                                                             maximum_length))

            result += "-" + self.transform_hundreds_upper(number % (10 ** hundredsUpper[pos][0]),
                                                          pos + 1,
                                                          hundredsUpper,
                                                          maximum_length)
        elif pos == len(hundredsUpper) - 1:
            if hundreds != 0:
                result += "-" + self.generate_text_given_position(self.transform(hundreds,
                                                                                 pos,
                                                                                 hundredsUpper,
                                                                                 maximum_length) + "-" + \
                                                                  hundredsUpper[-1][1], self.transform(hundreds,
                                                                                                       pos,
                                                                                                       hundredsUpper,
                                                                                                       maximum_length))

            result += "-" + self.generate_text_given_position(self.transform(number % minimum_value,
                                                                             pos,
                                                                             hundredsUpper,
                                                                             maximum_length),
                                                              self.transform(number % minimum_value,
                                                                             pos,
                                                                             hundredsUpper,
                                                                             maximum_length))

        return result
