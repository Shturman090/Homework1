import random
# 1_____________________________________________________________
class Animal:
    live = True
    sound = None            # звук(изначально отсутствует)
    _DEGREE_OF_DANGER = 0   # степень опасности существа

    def __init__(self, speed):
        self.speed = speed
        self._cords = [0, 0, 0]  # координаты в пространстве

    def move (self, dx, dy, dz):
        if dz < 0:
            print(f"It's too deep, i can't dive")
        else:
            self._cords = [self.speed * dx, self.speed * dy, self.speed * dz]

    def get_cords(self):
        print(f'X: {self._cords [0]}, Y: {self._cords [1]}, Z: {self._cords [2]}')

    def attack (self):
        if self._DEGREE_OF_DANGER < 5:
            print(f"Sorry, i'm peaceful :)")
        else:
            print(f"Be careful, i'm attacking you 0_0")

    def speak (self):
        print(self.sound)

# 2 __________________________________________________________________
class Bird (Animal):
    beak = True
    def lay_eggs (self):
        random_integer = random.randint (1, 4)
        print(f"Here are(is) {random_integer} eggs for you")

# 3 ____________________________________________________________________
class AquaticAnimal (Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):         #dz изменение координаты z в _cords
        self.dz = dz
        self._cords[2] = int(abs(dz) * self.speed * 0.5 - self._cords[2])


# 4 ____________________________________________________________________
class PoisonousAnimal (Animal):
    _DEGREE_OF_DANGER = 8

# 5 ____________________________________________________________________
class Duckbill (Bird, PoisonousAnimal, AquaticAnimal):
    sound = "Click-click-click"

# Пример работы программы:
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