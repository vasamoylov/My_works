from threading import Thread, Lock
import random
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()
        self.oper_take_ = 0

    def deposit(self):
        if self.lock.locked():
            self.lock.release()
        for i in range(100):
            summ = random.randint(50, 500)
            self.balance += summ
            print(f'Пополнение: {summ}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        if self.oper_take_ < 100:
            sub_ = random.randint(50, 500)
            print(f'Запрос на снятие {sub_}')
            if sub_ <= self.balance:
                self.balance -= sub_
                # print(self.lock_.locked(), self.balance)
                print(f'Снятие: {sub_} руб. Баланс: {self.balance}')
            else:
                # print(self.lock_.locked(), self.balance)
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            self.oper_take_ += 1
            self.take()
        else:
            return


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')