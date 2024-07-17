from stanfordkarel import *
import os

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()    

def fill_pothole():
    turn_right()
    move()
    put_beeper()
    turn_around()
    move()
    turn_right()

def main():
    """ Karel code goes here! """
    move()
    fill_pothole()
    move()
    move()
    move()
    fill_pothole()
    move()

    pass

if __name__ == "__main__":
    run_karel_program(os.path.join(os.getcwd(), 'worlds/karel_03'))