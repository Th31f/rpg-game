from cmd import *
from textwrap import *
from sys import *
from os import *
from time import *
from random import *

screen_width = 100

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
aStats = [a.hp, a.damage, a.energy, a.magic_damage, a.arrow_damage, a.stealing, a.speed]d]

class Mage(PlayerClass):
    def __init__(self, hp = 75, damage = 30, energy = 100, magic damage = 75):
        self.hp = int(hp)
        self.damage = int(damage)
        self.energy = int(energy)
        self.magic_damage = int(magic_damage)
        self.arrow_damage = int(arrow_damage)
        self.stealing = int(stealing)
        self.speed = int(speed)
m = Mage()
aStats = [a.hp, a.damage, a.energy, a.magic_damage, a.arrow_damage, a.stealing, a.speed]

class Archer(PlayerClass):
    def __init__(self, hp = 150, damage = 20, energy = 100, magic_damage = 0, arrow_damage = 75, stealing = 20):
        self.hp = int(hp)
        self.damage = int(damage)
        self.energy = int(energy)
        self.magic_damage = int(magic_damage)
        self.arrow_damage = int(arrow_damage)
        self.stealing = int(stealing)
        self.speed = int(speed)
a = Archer()
aStats = [a.hp, a.damage, a.energy, a.magic_damage, a.arrow_damage, a.stealing, a.speed]

class Thief(PlayerClass):
    def __init__(self, hp = 125, damage = 35, energy = 100, magic_damage = 10, arrow_damage = 10, stealing = 50, speed = 125):
        self.hp = int(hp)
        self.damage = int(damage)
        self.energy = int(energy)
        self.magic_damage = int(magic_damage)
        self.arrow_damage = int(arrow_damage)
        self.stealing = int(stealing)
        self.speed = int(speed)
a = Thief()
aStats = [a.hp, a.damage, a.energy, a.magic_damage, a.arrow_damage, a.stealing, a.speed]

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
