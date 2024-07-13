import math
class Figure:
    sides_count = 0
    def __init__(self, color=(0, 0, 0), *sides):
        if len(sides) != self.sides_count:
            self.__sides = [list(sides)[0]] * self.sides_count
        elif len(sides) == self.sides_count:
            self.__sides = list(sides)
        self.__color = list(color)
        self.filled = False
    def get_color(self):
        return self.__color
    def __is_valid_color(self, r, g, b):
        if type(r) == int and type(g) == int and type(b) == int:
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                return True
    def set_color(self,r, g, b):
        if self.__is_valid_color(r, g, b) == True:
            self.__color.clear()
            self.__color.extend([r, g, b])
    def __is_valid_sides(self, *sides):
        a = True
        if len(sides) == len(self.__sides):
            for i in sides:
                if type(i) != int or i <= 0:
                    a = False
                break
        else:
            a = False
        return a
    def get_sides(self):
        return self.__sides
    def len(self):
        return sum(self.__sides)
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides) == True:
            if len(new_sides) == self.sides_count:
                self.__sides.clear()
                self.__sides.extend(new_sides)

class Circle(Figure):
    sides_count = 1
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = True
    def get_radius(self):
        self.__radius = self.get_sides()[0] / (2 * math.pi)
        return self.__radius
    def get_square(self):
        square = self.get_radius() ** 2 * math.pi
        return square
class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__heigh = True
    def get_heigh(self):
        a = self.get_sides()[0]
        b = self.get_sides()[1]
        c = self.get_sides()[2]
        p = (a + b + c) / 2
        self.__heigh = (2 * math.sqrt(p * (p - a) * (p - b) * (p - c))) / a
        return self.__heigh
    def get_square(self):
        a = self.get_sides()[0]
        h = self.get_heigh()
        square = (a * h) / 2
        return square
class Cube(Figure):
    sides_count = 12
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
    def get_volume(self):
        volume = self.get_sides()[0] ** 3
        return volume

circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())

print(circle1.len())

print(cube1.get_volume())
