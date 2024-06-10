from strategies.kata_strategy import KataStrategy


class OthersStrategy(KataStrategy):
    def __init__(self, units_strategy, tens_strategy):
        self.units_strategy = units_strategy
        self.tens_strategy = tens_strategy

    # 17 -> 19 ; 22  -> 29 ; 32 -> 39 , 42 -> 49 ...
    def transform(self, number):
        return self.tens_strategy.transform((number // 10)*10) + "-" + self.units_strategy.transform(number % 10)
