import math


class Figure :
    sides_count = 0

    def __init__(self, color:tuple,*sides:int):

        self.__color = color
        self.__sides = []
        for side in sides :
            self.__sides.append(side)
        self.filled = False

    def get_color(self):
        return  self.__color

    def __is_valid_color(self, r: int, g: int, b: int):
        if -1 < r < 256 and -1 < g < 256 and -1 < b < 256:
            return True
        else:
            return False

    def set_color(self,r,g,b):
        if self.__is_valid_color(r,g,b):
            self.__color = [r,g,b]

    def __is_valid_slides(self, *sides):
        for side in sides:
            if side <= 0:
                return False

        if self.__sides != len(sides):
            return False
        return  True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        perimeter = 0
        for side in self.__sides:
            perimeter = perimeter + side
        return perimeter

    def set_sides(self, *new_sides):
        number_sides = len(new_sides)
        if self.sides_count == number_sides:
            for number_side in range(number_sides):
                self.__sides[number_side] = new_sides[number_sides-1]

class Circle(Figure):
    sides_count = 1

    def __init__(self, color:tuple,*sides:int):
        super().__init__(color,*sides)
        self.radius = self.__len__() / math.pi

    def get_square(self):
        return math.pi * (self.radius ** 2)

class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        p = self.__len__()
        a = self.get_sides()[0]
        b = self.get_sides()[1]
        c = self.get_sides()[2]

        return (p * (p - a) * (p - b) * (p - c)) ** 0.5


class Cube(Figure) :
    sides_count = 12

    def __init__(self,color:tuple,side):
        super().__init__(color,side)
        self.__sides =[]
        for _ in range(12):
            self.__sides.append(side)
            print(self.__sides)

    def get_volume(self):
        a = self.get_sides()[0]
        return a ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)

cube1 = Cube((222, 35, 130), 6)



# Проверка на изменение цветов:

circle1.set_color(55, 66, 77) # Изменится

print(circle1.get_color())

cube1.set_color(300, 70, 15) # Не изменится

print(cube1.get_color())



# Проверка на изменение сторон:

cube1.set_sides(5, 3, 12, 4, 5) # Не изменится

print(cube1.get_sides())

circle1.set_sides(15) # Изменится

print(circle1.get_sides())



# Проверка периметра (круга), это и есть длина:

print(len(circle1))



# Проверка объёма (куба):

print(cube1.get_volume())

