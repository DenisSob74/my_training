class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def go_to(self, new_floor):
        floor = 0
        if new_floor <= 0:
            return print(f'В доме "{self.name}" "Такого этажа не существует"')
        if new_floor <= self.number_of_floor:
            print(f'В {self.name} {self.number_of_floor} этажа(-ей)')
            for floor in range(new_floor):
                print(floor + 1)
            print(f'поднимаемся на {new_floor} этаж')
        else:
            print(f'В доме "{self.name}" "Такого этажа не существует"')

    def __str__(self, *args, **kwargs):
        return f'Название {str(self.name)}, количество этажей {str(self.number_of_floor)}'

    def __len__(self):
        return self.number_of_floor

    def __eq__(self, other):
        return self.number_of_floor == other.number_of_floor

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floor = self.number_of_floor + value
        return self

    def __iadd__(self, value):
        return self.__add__(value)

    def __radd__(self, value):
        return self.__add__(value)

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floor > other.number_of_floor

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floor >= other.number_of_floor

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floor < other.number_of_floor

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floor <= other.number_of_floor

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floor != other.number_of_floor

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

h1.go_to(12)
h2.go_to(-1)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
# __eq__
print(h1 == h2)
# __add__
h1 = h1 + 10
print(h1)
print(h1 == h2)
# __iadd__
h1 += 10
print(h1)
# __radd__
h2 = 10 + h2
print(h2)
# __gt__
print(h1 > h2)
# __ge__
print(h1 >= h2)
# __lt__
print(h1 < h2)
# __le__
print(h1 <= h2)
# __ne__
print(h1 != h2)




