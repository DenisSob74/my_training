class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def __str__(self, *args, **kwargs): # real signature unknown
        return f'Название {str(self.name)}, количество этажей {str(self.number_of_floor)}'

    def __len__(self):
        return self.number_of_floor

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
