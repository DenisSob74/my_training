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



h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(12)
h2.go_to(-1)











