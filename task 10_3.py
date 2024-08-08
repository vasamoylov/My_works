from threading import Thread, Lock
import random
import time

lock = Lock()


class Bank:
    def __init__(self):
        self.balance = 0

    def deposit(self):
        if lock.locked():
            lock.release()
        for i in range(100):
            summ = random.randint(50, 500)
            self.balance += summ
            print(f'Пополнение: {summ}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            summ = random.randint(50, 500)
            print(f'Запрос на {summ}')
            if lock.locked():
                lock.release()
            if self.balance >= summ:
                self.balance -= summ
                print(f'Снятие: {summ}. Баланс: {self.balance}')
                time.sleep(0.001)
            else:
                lock.acquire()
                print('Запрос отклонён, недостаточно средств')
                time.sleep(0.001)

bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')