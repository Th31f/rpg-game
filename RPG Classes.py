class PlayerClass:
    def __init__(self, hp = 100, damage = 0, energy = 100, magic_damage = 0, arrow_damage = 0, stealing = 0, speed = 0):
        self.hp = int(hp)
        self.damage = int(damage)
        self.energy = int(energy)
        self.magic_damage = int(magic_damage)
        self.arrow_damage = int(arrow_damage)
        self.stealing = int(stealing)
        self.healing = int(healing)
        self.speed = int(speed)
        self.location = int(start)
pc = PlayerClass()
pcStats = [pc.hp, pc.damage, pc.energy, pc.magic_damage, pc.arrow_damage, pc.stealing, pc.healing, pc.speed]

class Knight(PlayerClass):
    def __init__(self, hp = 200, damage = 50, energy = 100, magic_damage = 0, arrow_damage = 0, stealing = 15, healing = 0, speed = 75):
        self.hp = int(hp)
        self.damage = int(damage)
        self.energy = int(energy)
        self.magic_damage = int(magic_damage)
        self.arrow_damage = int(arrow_damage)
        self.stealing = int(stealing)
        self.healing = int(healing)
        self.speed = int(speed)
k = Knight()
kStats = [k.hp, k.damage, k.energy, k.magic_damage, k.arrow_damage, k.stealing, k.healing, k.speed]

class Mage(PlayerClass):
    def __init__(self, hp = 100, damage = 20, energy = 100, magic_damage = 75, arrow_damage = 0, stealing = 10, healing = 15, speed = 50):
        self.hp = int(hp)
        self.damage = int(damage)
        self.energy = int(energy)
        self.magic_damage = int(magic_damage)
        self.arrow_damage = int(arrow_damage)
        self.stealing = int(stealing)
        self.healing = int(healing)
        self.speed = int(speed)
m = Mage()
mStats = [m.hp, m.damage, m.energy, m.magic_damage, m.arrow_damage, m.stealing, m.healing, m.speed]

class Archer(PlayerClass):
    def __init__(self, hp = 125, damage = 20, energy = 100, magic_damage = 0, arrow_damage = 75, stealing = 15, healing = 0, speed = 100):
        self.hp = int(hp)
        self.damage = int(damage)
        self.energy = int(energy)
        self.magic_damage = int(magic_damage)
        self.arrow_damage = int(arrow_damage)
        self.stealing = int(stealing)
        self.healing = int(healing)
        self.speed = int(speed)
a = Archer()
aStats = [a.hp, a.damage, a.energy, a.magic_damage, a.arrow_damage, a.stealing, a.healing, a.speed]

class Thief(PlayerClass):
    def __init__(self, hp = 125, damage = 35, energy = 100, magic_damage = 10, arrow_damage = 10, stealing = 75, healing = 0, speed = 150):
        self.hp = int(hp)
        self.damage = int(damage)
        self.energy = int(energy)
        self.magic_damage = int(magic_damage)
        self.arrow_damage = int(arrow_damage)
        self.stealing = int(stealing)
        self.healing = int(healing)
        self.speed = int(speed)
t = Thief()
tStats = [t.hp, t.damage, t.energy, t.magic_damage, t.arrow_damage, t.stealing, t.healing, t.speed]

class Giant(PlayerClass):
    def __init__(self, hp = 500, damage = 50, energy = 100, magic_damage = 0, arrow_damage = 0, stealing = 0, healing = 0, speed = 20):
        self.hp = int(hp)
        self.damage = int(damage)
        self.energy = int(energy)
        self.magic_damage = int(magic_damage)
        self.arrow_damage = int(arrow_damage)
        self.stealing = int(stealing)
        self.healing = int(healing)
        self.speed = int(speed)
g = Giant()
gStats = [g.hp, g.damage, g.energy, g.magic_damage, g.arrow_damage, g.stealing, g.healing, g.speed]

class Healer(PlayerClass):
    def __init__(self, hp = 75, damage = 20, energy = 100, magic_damage = 35, arrow_damage = 0, stealing = 0, healing = 75, speed = 125):
        self.hp = int(hp)
        self.damage = int(damage)
        self.energy = int(energy)
        self.magic_damage = int(magic_damage)
        self.arrow_damage = int(arrow_damage)
        self.stealing = int(stealing)
        self.healing = int(healing)
        self.speed = int(speed)
h = Healer()
hStats = [h.hp, h.damage, h.energy, h.magic_damage, h.arrow_damage, h.stealing, h.healing, h.speed]

