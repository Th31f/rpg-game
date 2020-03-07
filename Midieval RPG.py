class player1():
     def __init__(self, hp = 100, damage = 0, energy = 100, magic_damage = 0, arrow_damage = 0, stealing = 0, speed = 0, ):
        self.hp = int(hp)
        self.damage = int(damage)
        self.energy = int(energy)
        self.magic_damage = int(magic_damage)
        self.arrow_damage = int(arrow_damage)
        self.speed = int(speed)
        self.stealing = int(stealing)
        
p = player1()
pStats = [p.hp, p.damage, p.energy, p.magic_damage, p.arrow_damage, p.stealing, p.speed]

class Knight(player1):
    def __init__(self, hp = 175, damage = 75, energy = 100, magic_damage = 0, arrow_damage = 0, stealing = 20, speed = 30):
        self.hp = int(hp)
        self.damage = int(damage)
        self.energy = int(energy)
        self.magic_damage = int(magic_damage)
        self.arrow_damage = int(arrow_damage)
        self.speed = int(speed)
        self.stealing = int(stealing)
k = Knight()
kStats = [k.hp, k.damage, k.energy, k.magic_damage, k.arrow_damage, k.stealing, k.speed]

class Mage(player1):
    def __init__(self, hp = 75, damage = 10, energy = 100, magic_damage = 75, arrow_damage = 0, stealing = 10, speed = 20):
        self.hp = int(hp)
        self.damage = int(damage)
        self.energy = int(energy)
        self.speed = int(speed)
        self.magic_damage = int(magic_damage)
        self.arrow_damage = int(arrow_damage)
        self.speed = int(speed)
        self.stealing = int(stealing)
m = Mage()
mStats = [m.hp, m.damage, m.energy, m.magic_damage, m.arrow_damage, m.stealing, m.speed]

class Archer(player1):
    def __init__(self, hp = 100, damage = 20, energy = 100, magic_damage = 75, arrow_damage = 75, stealing = 30,speed = 35):
        self.hp = int(hp)
        self.damage = int(damage)
        self.energy = int(energy)
        self.magic_damage = int(magic_damage)
        self.arrow_damage = int(arrow_damage)
        self.speed = int(speed)
        self.stealing = int(stealing)
a = Archer()
aStats = [a.hp, a.damage, a.energy, a.magic_damage, a.arrow_damage, a.stealing, a.speed]

class Thief(player1):
    def __init__(self, hp = 125, damage = 25, energy = 100, magic_damage = 0, arrow_damage = 0, stealing = 75, speed = 50):
        self.hp = int(hp),
        self.damage = int(damage)
        self.energy = int(energy)
        self.magic_damage = int(magic_damage)
        self.arrow_damage = int(arrow_damage)
        self.speed = int(speed)
        self.stealing = int(stealing)
t = Thief()
tStats = [t.hp, t.damage, t.energy, t.magic_damage, t.arrow_damage, t.stealing, t.speed]

print("Please Select a Class")
print("Choose Wisely")
print("Knight (1)")
print("Mage (2)")
print("Archer (3)")
print("Thief (4)")
choice = int(input("Enter choice( 1, 2, 3, 4 ):"))
print("-----------------------------------------------------")


