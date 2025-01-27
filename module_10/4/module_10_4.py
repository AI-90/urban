import threading
from time import sleep
from random import randint
from queue import Queue
class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(threading.Thread):
    def __init__(self, name_guest):
        threading.Thread.__init__(name_guest)
        self.name = name_guest
    def run(self):
        sleep(randint(3,10))

class Cafe:
    def __init__(self, *table):
        self.tables = table
        self.queue = Queue()

    def guest_arrival(self, *guests):

    def discuss_guests:

# Создание столов

tables = [Table(number) for number in range(1, 6)]

# Имена гостей

guests_names = [

'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',

'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'

]

# Создание гостей

guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами

cafe = Cafe(*tables)

# Приём гостей

cafe.guest_arrival(*guests)

# Обслуживание гостей

cafe.discuss_guests()