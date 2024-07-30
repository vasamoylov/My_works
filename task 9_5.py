class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step
        if step == 0:
            raise StepValueError()
        self.pointer = self.start

    def __iter__(self):
        self.pointer = self.start
        return self
    def __next__(self):
        if self.step < 0:
           if self.stop <= self.pointer + self.step:
               self.pointer += self.step
               return self.pointer
           else:
               raise StopIteration()
        else:
            if self.stop >= self.pointer + self.step:
                self.pointer += self.step
                return self.pointer
            else:
                raise StopIteration()

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
#iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
'''for i in iter5:
    print(i, end=' ')
print()'''




