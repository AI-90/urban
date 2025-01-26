import threading
from time import sleep

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        days = 0
        enemies = 100
        print(f"{self.name}, на нас напали!")
        while enemies > 0:
            days += 1
            enemies -= self.power
            sleep(1)
            print(f"{self.name} сражается {days} дней(дня), осталось {enemies} воинов.")
        print(f"{self.name}, одержал победу спустя {days} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
print("Битвы закончились!")