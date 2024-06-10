from strategies.kata_strategy import KataStrategy


class TensStrategy(KataStrategy):
    # 10 - 90
    def __init__(self, tens):
        self.tens = tens

    def transform(self, number):
        return self.tens[number//10]
