from turtle import speed


class Animal:
    live = True
    sound = None                # звук (изночально остсутствует)
    _DEGREE_OF_DANGER = 0       # степень опасности существа

    def __init__(self, name):
        self.name = name
        self.speed = speed
        self.cords = [0, 0, 0]      # координаты в пространстве



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





class Bird(Animal):
    beak = False  # наличие клюва


    def lay_eggs(self):
        print("Here are(is) <случайное число от 1 до 4> eggs for you")


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3


    def dive_in(self, dz):
        dz = abs(dz)
        self.cords['z'] -= dz*0.5


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"         # - звук, который издаёт утконос




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
