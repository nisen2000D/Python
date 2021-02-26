from abc import ABC, abstractmethod


class Clothing(ABC):
    def __init__(self, param):
        self.param = param

    @property
    def consumption(self):
        return f'Всего расход ткани: {self.param / 6.5 + 0.5 + 2 * self.param + 0.3}'

    @abstractmethod
    def abstract(self):
        pass


class Coat(Clothing):
    def consumption(self):
        return f'Расход ткани для пальто: {self.param / 6.5 + 0.5}'

    def abstract(self):
        return ''


class Costume(Clothing):
    def consumption(self):
        return f'Расход ткани для костюма: {2 * self.param + 0.3}'

    def abstract(self):
        pass


coat = Coat(34)
costume = Costume(160)
print(costume.consumption())
print(coat.consumption())
print(coat.abstract())
