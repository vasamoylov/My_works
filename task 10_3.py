from threading import Thread, Lock
import random
import time


class Bank():

    def __init__(self, start_balance, lock):
        self.balance = start_balance
        self.lock = lock
        self.add_deposit = 0
        self.take_summ = 0

    def deposit(self):
        if self.add_deposit < 100:
            add_ = random.randint(50, 500)
            self.balance += add_
            print(f'Пополнение: {add_} руб. Баланс: {self.balance} руб.')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)
            self.add_deposit += 1
            self.deposit()
        else:
            return

    def take(self):
        if self.take_summ < 100:
            summ = random.randint(50, 500)
            print(f'Запрос на снятие {summ}')
            if summ <= self.balance:
                self.balance -= summ
                print(f'Снятие: {summ} руб. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            self.take_summ += 1
            self.take()
        else:
            return


lock_ = Lock()
bank_ = Bank(0, lock_)

take_ = Thread(target=Bank.take, args=(bank_,))
deposit_ = Thread(target=Bank.deposit, args=(bank_,))

take_.start()
deposit_.start()

deposit_.join()
take_.join()

print(f'Итоговый баланс: {bank_.balance}')
