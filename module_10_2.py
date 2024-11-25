# ЗАДАНИЕ ПО ТЕМЕ "Потоки на классах"

import threading
import time


class Knight(threading.Thread):

    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name  # имя рыцаря
        self.power = power  # сила рыцаря

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemy_count = 100  # количество врагов
        day = 0  # день битвы
        while enemy_count:
            day += 1
            enemy_count -= self.power
            time.sleep(1)
            print(f'{self.name} сражается {day}..., осталось {enemy_count} воинов.')
        print(f'{self.name} одержал победу спустя {day} дней(дня)!')


# Создание объектов класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запускаем потоки
first_knight.start()
second_knight.start()
# Ждём завершения потоков
first_knight.join()
second_knight.join()
# Вывод строки об окончании сражения
print('Все битвы закончились!')
