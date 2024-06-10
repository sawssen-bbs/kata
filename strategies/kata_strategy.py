from abc import ABC, abstractmethod


class KataStrategy(ABC):
    @abstractmethod
    def transform(self, number):
        pass
