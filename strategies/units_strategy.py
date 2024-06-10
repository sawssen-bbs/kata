from strategies.kata_strategy import KataStrategy


class UnitStrategy(KataStrategy):
    # 0 - 16
    def __init__(self, units):
        self.units = units

    def transform(self, number):
        return self.units[number]
