from cmd import *
from textwrap import *
from sys import *
from os import *
from time import *
from random import *

screen_width = 100

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
