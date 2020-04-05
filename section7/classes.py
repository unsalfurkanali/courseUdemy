class car():
    def __init__(self, model, renk, hp=100):
        self.model = model
        self.renk = renk
        self.hp = hp

araba = car("Range Rover", "Siyah")
print(araba.hp)