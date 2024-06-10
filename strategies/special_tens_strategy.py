from strategies.kata_strategy import KataStrategy


class SpecialTenStrategy(KataStrategy):
    def __init__(self, units_strategy, tens_strategy, other_strategy):
        self.units_strategy = units_strategy
        self.tens_strategy = tens_strategy
        self.other_strategy = other_strategy

    def transform(self, number):
        # 70 -> 99:
        if number == 71:
            return self.tens_strategy.transform(60) + "-et-" + \
                   self.units_strategy.transform(number % 60)
        if number <= 76:
            return self.tens_strategy.transform(60) + "-" + \
                   self.units_strategy.transform(number % 60)
        if number < 80:
            return self.tens_strategy.transform(60) + "-" + \
                   self.other_strategy.transform(number % 60)
        elif number <= 86:
            return self.units_strategy.transform(4) + "-" + \
                   self.tens_strategy.transform(20) + "-" + \
                   self.units_strategy.transform(number % 80) if number % 80 != 0 else self.units_strategy.transform(4) + "-" + \
                   self.tens_strategy.transform(20)
        elif number <= 96:
            return self.units_strategy.transform(4) + "-" + \
                   self.tens_strategy.transform(20) + "-" + \
                   self.units_strategy.transform(number % 80)
        else:
            return self.units_strategy.transform(4) + "-" + \
                   self.tens_strategy.transform(20) + "-" + \
                   self.other_strategy.transform(number % 80)
