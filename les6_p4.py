
'''
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''

class Car:
    _count = 0
    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        Car._count += 1
    def hello(self):
        print("Родительский метод класса Car")
    def go(self):
        print("The car is moving.")
    def stop(self):
        print("The car was stopped.")
    def turn(self, direct: str):
        print(f"The car turned to the {direct}.")
    def show_speed(self):
        print("Current speed:", self.speed, 'km/h.')


class TownCar(Car):
    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        super().__init__(speed, color, name, is_police)
    def hello(self):
        print("Родительский метод класса TownCar")
    def show_speed(self):
        if self.speed > 60:
            print("Speeding!!! Reduce speed.")
        else:
            print("Current speed:", self.speed, 'km/h.')


class SportCar(Car):
    def hello(self):
        print("Родительский метод класса SportCar")


class WorkCar(Car):
    def hello(self):
        print("Родительский метод класса WorkCar")
    def show_speed(self):
        if self.speed > 40:
            print("Speeding!!! Reduce speed.")
        else:
            print("Current speed:", self.speed, 'km/h.')


class PoliceCar(Car):
    def hello(self):
        print("Родительский метод класса PoliceCar")


c = Car(36, "magenda", "Golf", False)
c.speed = 60
print(c.speed)



town = TownCar(61, "white", "Audi", False)
town.hello()
town.go()
town.stop()
town.show_speed()
town.turn('right')
print(town._count)


town.speed = 50
town.show_speed()


Sport = SportCar(250, "red", "Ferrari", False)
Sport.hello()
Sport.go()
Sport.stop()
Sport.show_speed()
Sport.turn('right')
print(town._count)


Work = WorkCar(35, "blue", "Honda", False)
Work.hello()
Work.go()
Work.stop()
Work.show_speed()
Work.turn('right')
print(Work._count)


Police = PoliceCar(100, "black", "Honda", True)
Police.hello()
Police.go()
Police.stop()
Police.stop()
Police.show_speed()
Police.turn('right')
print(Police._count)




