class PlayerClass:
    def __init__(self, hp = 100, damage = 0, energy = 100, magic_damage = 0, arrow_damage = 0, stealing = 0, speed = 0):
        self.hp = int(hp)
        self.damage = int(damage)
        self.energy = int(energy)
        self.magic_damage = int(magic_damage)
        self.arrow_damage = int(arrow_damage)
        self.stealing = int(stealing)
        self.speed = int(speed)
pc = PlayerClass()
pcStats = [pc.hp, pc.damage, pc.energy, pc.magic_damage, pc.arrow_damage, pc.stealing, pc.speed]

class Knight(PlayerClass):
    def __init__(self, hp = 225, damage = 50, energy = 100, ,magic_damage = 0, arrow_damage = 0):
        self.hp = int(hp)
        self.damage = int(damage)
        self.energy = int(energy)
        self.magic_damage = int(magic_damage)
        self.arrow_damage = int(arrow_damage)
        self.stealing = int(stealing)
        self.speed = int(speed)
s = Knight()
sStats = [s.hp, s.damage, s.energy, s.strength, a.speed]

class Mage(PlayerClass):
    def __init__(self, hp = 75, damage = 30, energy = 100, magic damage = 500):
        self.hp = int(hp)
        self.damage = int(damage)
        self.energy = int(energy)
        self.magic_damage = int(magic_damage)
        self.arrow_damage = int(arrow_damage)
        self.stealing = int(stealing)
        self.speed = int(speed)
m = Mage()
mStats = [m.hp, m.damage, m.energy, m.mana, a.speed]

class Archer(PlayerClass):
    def __init__(self, hp = 150, damage = 20, energy = 100, arrow_damage = 75):
        self.hp = int(hp)
        self.damage = int(damage)
        self.energy = int(energy)
        self.magic_damage = int(magic_damage)
        self.arrow_damage = int(arrow_damage)
        self.stealing = int(stealing)
        self.speed = int(speed)
a = Archer()
aStats = [a.hp, a.damage, a.energy, a.arrow_damage, a.speed]

class Thief(PlayerClass):
    def __init__(self, hp = 125, damage = 35, energy = 100, magic_damage = 0, stealing = 50, speed = 125):
        self.hp = int(hp)
        self.damage = int(damage)
        self.energy = int(energy)
        self.magic_damage = int(magic_damage)
        self.arrow_damage = int(arrow_damage)
        self.stealing = int(stealing)
        self.speed = int(speed)
a = Thief()
aStats = [a.hp, a.damage, a.energy, a.stealing, a.speed]
