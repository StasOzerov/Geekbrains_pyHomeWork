
'''
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
и метод running (запуск). Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
'''



import time

class TrafficLight:

    _color = "красный"

    def running(self):
        while True:
            print(TrafficLight._color)
            time.sleep(7)
            TrafficLight._color = "желтый"
            print(TrafficLight._color)
            time.sleep(2)
            TrafficLight._color = "зеленый"
            print(TrafficLight._color)
            time.sleep(5)
            TrafficLight._color = "красный"

exhibit = TrafficLight()
a = exhibit.running()


