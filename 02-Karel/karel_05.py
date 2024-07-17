from stanfordkarel import *
import os

def main():
    """ Karel code goes here! """
    for i in range(4):
        put_beeper()
        move()
        move()
        move()
        turn_left()
    pass

if __name__ == "__main__":
    run_karel_program(os.path.join(os.getcwd(), 'worlds/karel_05'))