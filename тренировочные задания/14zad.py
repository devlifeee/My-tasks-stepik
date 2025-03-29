class Frog:
    def sound(self):
        print("ква-ква")
class Sparrow:
    def sound(self):
        print("Чирик-чирик")
class Hedgehog:
    def sound(self):
        print("Фыр-фыр")

frog = Frog()
sparrow = Sparrow()
hedgehog =  Hedgehog()

animals = [frog, sparrow, hedgehog]

for animal in animals:
    animal.sound()

