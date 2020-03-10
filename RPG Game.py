from cmd import *
from textwrap import *
from sys import *
from os import *
from time import *
from random import *

screen_width = 100class PlayerClass:
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

def title_screen_selections():
    option = input ("> ")
    if option.lower() == ("play"):
        start_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid option.")
        option = input("> ")
        if option.lower() == ("play"):
            start_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()

def title_screen():
    os.system('clear')
    print("-------------------------------")
    print("  Welcome to whatever this is  ")
    print("-------------------------------")
    print("             -Play-            ")
    print("             -Help-            ")
    print("             -Quit-            ")
    title_screen_selections()

def help_menu():
    print("Use W, A, S, D to move.")
    print("Type your commands to use them.")

def start_game():
    
DESCRIPTION = 'desription'
EXAMINATION = 'examine'
SOLVED = 'False'
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {'a1':False, 'a2':False, 'a3':False, 'a4':False,
                'b1':False, 'b2':False, 'b3':False, 'b4':False,
                'c1':False, 'c2':False, 'c3':False, 'c4':False,
                'd1':False, 'd2':False, 'd3':False, 'd4':False,
                 }

zonemap = {
    'a1':{
        ZONENAME: ""
        DESCRIPTION = 'desription'
        EXAMINATION = 'examine'
        SOLVED = 'False'
        UP = ''
        DOWN = 'b1'
        LEFT = ''
        RIGHT = 'a2'
        },

    'a2':{
        ZONENAME: ""
        DESCRIPTION = 'desription'
        EXAMINATION = 'examine'
        SOLVED = 'False'
        UP = ''
        DOWN = 'b2'
        LEFT = 'a1'
        RIGHT = 'a3'
        },

    'a3':{
        ZONENAME: ""
        DESCRIPTION = 'desription'
        EXAMINATION = 'examine'
        SOLVED = 'False'
        UP = ''
        DOWN = 'b3'
        LEFT = 'a2'
        RIGHT = 'a4'
        },

    'a4':{
        ZONENAME: ""
        DESCRIPTION = 'desription'
        EXAMINATION = 'examine'
        SOLVED = 'False'
        UP = ''
        DOWN = 'b4'
        LEFT = 'a3'
        RIGHT = ''
        },

    'b1':{
        ZONENAME: ""
        DESCRIPTION = 'desription'
        EXAMINATION = 'examine'
        SOLVED = 'False'
        UP = 'a1'
        DOWN = 'c1'
        LEFT = ''
        RIGHT = 'b2'
        },

    'b2':{
        ZONENAME: "Home"
        DESCRIPTION = 'desription'
        EXAMINATION = 'examine'
        SOLVED = 'False'
        UP = 'a2'
        DOWN = 'c2'
        LEFT = 'b1'
        RIGHT = 'b3'
        },

    'b3':{
        ZONENAME: ""
        DESCRIPTION = 'desription'
        EXAMINATION = 'examine'
        SOLVED = 'False'
        UP = 'a3'
        DOWN = 'c3'
        LEFT = 'b2'
        RIGHT = 'b4'
        },

    'b4':{
        ZONENAME: ""
        DESCRIPTION = 'desription'
        EXAMINATION = 'examine'
        SOLVED = 'False'
        UP = 'a4'
        DOWN = 'c4'
        LEFT = 'b3'
        RIGHT = ''
        },

    'c1':{
        ZONENAME: ""
        DESCRIPTION = 'desription'
        EXAMINATION = 'examine'
        SOLVED = 'False'
        UP = 'b1'
        DOWN = 'd1'
        LEFT = ''
        RIGHT = 'c2'
        },

    'c2':{
        ZONENAME: ""
        DESCRIPTION = 'desription'
        EXAMINATION = 'examine'
        SOLVED = 'False'
        UP = 'b2'
        DOWN = 'd2'
        LEFT = 'c1'
        RIGHT = 'c3'
        },

    'c3':{
        ZONENAME: ""
        DESCRIPTION = 'desription'
        EXAMINATION = 'examine'
        SOLVED = 'False'
        UP = 'b3'
        DOWN = 'd3'
        LEFT = 'c2'
        RIGHT = 'c4'
        },

    'c4':{
        ZONENAME: ""
        DESCRIPTION = 'desription'
        EXAMINATION = 'examine'
        SOLVED = 'False'
        UP = 'b4'
        DOWN = 'd4'
        LEFT = 'c3'
        RIGHT = ''
        },

    'd1':{
        ZONENAME: ""
        DESCRIPTION = 'desription'
        EXAMINATION = 'examine'
        SOLVED = 'False'
        UP = 'c1'
        DOWN = ''
        LEFT = ''
        RIGHT = 'd2'
        },

    'd2':{
        ZONENAME: ""
        DESCRIPTION = 'desription'
        EXAMINATION = 'examine'
        SOLVED = 'False'
        UP = 'c2'
        DOWN = ''
        LEFT = 'd1'
        RIGHT = 'd3'
        },

    'd3':{
        ZONENAME: ""
        DESCRIPTION = 'desription'
        EXAMINATION = 'examine'
        SOLVED = 'False'
        UP = 'c3'
        DOWN = ''
        LEFT = 'd2'
        RIGHT = 'd4'
        },

    'd4':{
        ZONENAME: ""
        DESCRIPTION = 'desription'
        EXAMINATION = 'examine'
        SOLVED = 'False'
        UP = 'c4'
        DOWN = ''
        LEFT = 'd3'
        RIGHT = ''
        },
        }
