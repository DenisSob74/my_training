import random

class Animal:
    live = True
    _DEGREE_OF_DANGER = 0               # степень опасности существа

    def __init__(self, name, speed):
        self.name = name
        self.cords = [0, 0, 0]          # координаты в пространстве
        self.speed = speed

    def move(self, dx, dy, dz):

        new_x = self.cords + dx * self.speed
        new_y = self.cords + dy * self.speed
        new_z = self.cords + dz * self.speed

        if new_z < 0:
            print("It's too deep, i can't dive :(")

        else:
            self.cords = [new_x, new_y, new_z]

    def get_cords(self):
        return f"X: {self.cords}, Y: {self.cords}, Z: {self.cords}"

    def attack(self):
        degree_of_danger = sum(self.cords)
        if degree_of_danger < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self, sound=None):
        return sound  # звук (изночально остсутствует)

class Bird(Animal):
    beak = False                    # наличие клюва

    def lay_eggs(self):
        self.random_eggs = random.randint(1, 4)
        print(f"Here are(is) {self.random_eggs} eggs for you")


class AquaticAnimal(Animal):        # класс описывающий плавающего животного
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        dz = abs(dz)
        self.cords['z'] -= dz * 0.5


class PoisonousAnimal(Animal):      # класс описывающий ядовитых животных
    _DEGREE_OF_DANGER = 8


class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"     #  звук, который издаёт утконос


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)

db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()
