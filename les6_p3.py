
'''
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''

class Worker:

    def __init__(self, name, surname, position, _income: dict):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income


class Position(Worker):

    def get_full_name(self):
        print('Полное имя сотрудника:', self.name, self.surname)

    def get_total_income(self):
        try:
            print('Доход с учётом премии:', sum(self._income.values()))
        except TypeError:
            print('Некорректные значения в словаре!')


Ivan = Position('Иван', 'Иванов', 'инженер', {"оклад": 10000, "премия": 5000})

print(Ivan.name)
print(Ivan.surname)
print(Ivan.position)
print(Ivan._income)
Ivan.get_full_name()
Ivan.get_total_income()

