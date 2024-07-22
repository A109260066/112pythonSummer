from stanfordkarel import *
import os

def put_and_move():
    put_beeper()
    move()

def main():
    """ Karel code goes here! """
    while front_is_clear():
        put_and_move()
    put_beeper()    

    pass

if __name__ == "__main__":
    run_karel_program(os.path.join(os.getcwd(), 'worlds/karel_07'))