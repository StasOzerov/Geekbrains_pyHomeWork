
'''
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''

class Stationery:
    def __init__(self, title: str):
        self.title = title
    def draw(self):
        print("Запуск отрисовки.")

class Pen(Stationery):
    def draw(self):
        print("Ручка фирмы", self.title)
        print("Запуск отрисовки ручкой.")


class Pencil(Stationery):
    def draw(self):
        print("Карандаш фирмы", self.title)
        print("Запуск отрисовки карандашом.")


class Handle(Stationery):
    def draw(self):
        print("Маркер фирмы", self.title)
        print("Запуск отрисовки маркером.")



Stat = Stationery("канцелярская принадлежность")
Stat.draw()

Parker = Pen("Parker")
Parker.draw()

Cat = Pencil("Cat")
Cat.draw()

Yoo = Handle("Yoo")
Yoo.draw()
