import random


class Animal:
    live = True
    _DEGREE_OF_DANGER = 0  # степень опасности существа

    def __init__(self, speed):
        self._cords = [0, 0, 0]  # координаты в пространстве
        self.speed = speed

    def move(self, dx, dy, dz):

        new_x = self._cords[0] + dx * self.speed
        new_y = self._cords[1] + dy * self.speed
        new_z = self._cords[2] + dz * self.speed

        if new_z < 0:
            print("It's too deep, i can't dive :(")

        else:
            self._cords = [new_x, new_y, new_z]

    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {int(self._cords[2])}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Be careful, i'm attacking you 0_0")
        else:
            print("Sorry, i'm peaceful :)")

    def speak(self, sound=None):
        self.sound = sound
        return sound  # звук (изночально остсутствует)


class Bird(Animal):
    beak = True  # наличие клюва

    def lay_eggs(self):
        self.random_eggs = random.randint(1, 4)
        print(f"Here are(is) {self.random_eggs} eggs for you")


class AquaticAnimal(Animal):  # класс описывающий плавающего животного

    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords[2] -= abs(dz) * self.speed / 2
        return


class PoisonousAnimal(Animal):  # класс описывающий ядовитых животных
    _DEGREE_OF_DANGER = 8


class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    def __init__(self, speed, sound="Click-click-click"):  # звук, который издаёт утконос
        super().__init__(speed)
        self.sound = sound

    def speak(self, sound=None):
        print(self.sound)


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
