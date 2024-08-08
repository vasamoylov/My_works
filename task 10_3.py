from threading import Thread, Lock
import random
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        if self.lock.locked():
            self.lock.release()
        for i in range(100):
            summ = random.randint(50, 500)
            self.balance += summ
            print(f'Пополнение: {summ}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            summ = random.randint(50, 500)
            print(f'Запрос на {summ}')
            if self.balance >= summ:
                self.balance -= summ
                print(f'Снятие: {summ}. Баланс: {self.balance}')
                time.sleep(0.001)
            else:
                self.lock.acquire()
                print('Запрос отклонён, недостаточно средств')
                #time.sleep(0.001)


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
