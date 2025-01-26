import threading
from time import sleep
from random import randint
class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            plus = randint(50, 500)
            self.balance += plus
            print(f"Пополнение: {plus}. Баланс: {self.balance}")
            if self.balance >= 500 and self.lock.locked() == True:
                self.lock.release()
            sleep(0.001)

    def take(self):
        for _ in range(100):
            minus = randint(50, 500)
            print(f"Запрос на {minus}")
            if minus <= self.balance:
                self.balance -= minus
                print(f"Снятие: {minus}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            sleep(0.001)




bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))



th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')