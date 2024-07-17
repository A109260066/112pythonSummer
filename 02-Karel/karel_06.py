from stanfordkarel import *
import os

def put_5_beeper():
    for i in range(5):
        put_beeper()

def move_to_next_corner():
    move()
    move()
    move()
    turn_left()

def main():
    """ Karel code goes here! """
    for i in range(4):
        put_5_beeper()
        move_to_next_corner()
    pass

if __name__ == "__main__":
    run_karel_program(os.path.join(os.getcwd(), 'worlds/karel_06'))