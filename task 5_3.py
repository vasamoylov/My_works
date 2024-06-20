class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType
    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors or self.buildingType == other.buildingType

h1 = Building(10, 'Монолит')
h2 = Building(3, 'Кирпич')
print(h1 == h2)