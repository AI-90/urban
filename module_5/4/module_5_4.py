class House():

    houses_history = []

    def __new__(cls, name, number_of_floors):
        cls.houses_history.append(name)
        return object.__new__(cls)


    def __init__(self,name,number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self,new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for i in range(1,new_floor+1):
                print(i)

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if not(isinstance(other, House)):
            return NotImplemented
        elif self.number_of_floors == other.number_of_floors:
            return True
        else:
            return False

    def __lt__(self, other):
        if not (isinstance(other, House)):
            return NotImplemented
        elif self.number_of_floors < other.number_of_floors:
            return True
        else:
            return False

    def __le__(self, other):
        if not(isinstance(other, House)):
            return NotImplemented
        elif self.number_of_floors <= other.number_of_floors:
            return True
        else:
            return False

    def __gt__(self, other):
        if not (isinstance(other, House)):
            return NotImplemented
        elif self.number_of_floors > other.number_of_floors:
            return True
        else:
            return False

    def __ge__(self, other):
        if not (isinstance(other, House)):
            return NotImplemented
        elif self.number_of_floors >= other.number_of_floors:
            return True
        else:
            return False

    def __ne__(self, other):
        if not (isinstance(other, House)):
            return NotImplemented
        elif self.number_of_floors != other.number_of_floors:
            return True
        else:
            return False

    def __add__(self, value):
        if not (isinstance(value, int)):
            return NotImplemented
        else:
            self.number_of_floors += value
            return self

    def __radd__(self, value):
        if not (isinstance(value, int)):
            return NotImplemented
        else:
            self.number_of_floors += value
            return self

    def __iadd__(self, value):
        if not (isinstance(value, int)):
            return NotImplemented
        else:
            self.number_of_floors += value
            return self

    def __sub__(self, value):
        if not (isinstance(value, int)):
            return NotImplemented
        else:
            self.number_of_floors -= value
            return self

    def __rsub__(self, value):
        if not (isinstance(value, int)):
            return NotImplemented
        else:
            self.number_of_floors -= value
            return self

    def __isub__(self, value):
        if not (isinstance(value, int)):
            return NotImplemented
        else:
            self.number_of_floors -= value
            return self

    def __mul__(self, value):
        if not (isinstance(value, int)):
            return NotImplemented
        else:
            self.number_of_floors *= value
            return self

    def __rmul__(self, value):
        if not (isinstance(value, int)):
            return NotImplemented
        else:
            self.number_of_floors *= value
            return self

    def __imul__(self, value):
        if not (isinstance(value, int)):
            return NotImplemented
        else:
            self.number_of_floors *= value
            return self

    def __truediv__(self, value):
        if not (isinstance(value, int)):
            return NotImplemented
        else:
            self.number_of_floors /= value
            return self

    def __rtruediv__(self, value):
        if not (isinstance(value, int)):
            return NotImplemented
        else:
            self.number_of_floors /= value
            return self

    def __itruediv__(self, value):
        if not (isinstance(value, int)):
            return NotImplemented
        else:
            self.number_of_floors /= value
            return self


h1 = House('ЖК Эльбрус', 10)

print(House.houses_history)

h2 = House('ЖК Акация', 20)

print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)

print(House.houses_history)

# Удаление объектов
del h2
del h3
print(House.houses_history)
