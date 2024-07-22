from stanfordkarel import *
import os

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def climb():
    turn_left()
    move()
    turn_right()
    move()
    pick_beeper()

def main():
    """ Karel code goes here! """
    #for i in range(4):
    #    climb()
    
    while front_is_blocked():
        climb()

    pass

if __name__ == "__main__":
    run_karel_program(os.path.join(os.getcwd(), 'worlds/karel_08'))