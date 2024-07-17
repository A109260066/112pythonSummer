from stanfordkarel import *
import os

def main():
    """ Karel code goes here! """
    move()
    for i in range(42):
        put_beeper()
    move()
    pass

if __name__ == "__main__":
    run_karel_program(os.path.join(os.getcwd(), 'worlds/karel_04'))