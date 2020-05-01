
'''
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда,
которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
'''

from abc import ABC, abstractmethod


class Dress(ABC):

    def class_info(self):
        print('Расчёт расхода ткани.')

    @abstractmethod
    def object_info(self) -> None:
        pass

    @abstractmethod
    def calc(self) -> float:
        pass

    def __add__(self, other):
        return other + self.calc()


class Coat(Dress):

    def object_info(self):
        print('Тип одежды - пальто.')

    def __init__(self, v):
        if isinstance(v, (int, float)) is False or v < 0:
            raise ValueError
        self.v = v

    def calc(self):
        return self.v/6.5 + 0.5

    def __str__(self):
        return f'Пальто. Расход: {self.calc():>.2f} кв. м.'

    def calc_print(self):
        return f'Расход {self.calc():>.2f} кв.м для размера {self.v}\n'


class Suit(Dress):

    def object_info(self):
        print('Тип одежды - костюм.')

    def __init__(self, h):
        if isinstance(h, (int, float)) is False or h < 0:
            raise ValueError
        self.h = h

    def calc(self):
        return 2*self.h + 0.3

    def __str__(self):
        return f'Костюм. Расход: {self.calc():>.2f} кв. м.'

    def calc_print(self):
        return f'Расход {self.calc():>.2f} кв.м для роста {self.h}\n'


coat1 = Coat(5)
coat1.class_info()
coat1.object_info()
print(coat1.calc())
print(coat1.calc_print())

suit1 = Suit(2)
suit1.class_info()
suit1.object_info()
print(suit1.calc())
print(suit1.calc_print())

print(coat1)
print(suit1)
print(coat1 + suit1)
