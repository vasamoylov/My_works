class House:
    def __init__(self):
        self.numberOfFloors = 0
        print(self.numberOfFloors)
    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(self.numberOfFloors)

h = House()
h.setNewNumberOfFloors(input('Введите этажность '))


