from stanfordkarel import *
import os

def collect_line_of_beepers():
    while beepers_present():
        pick_beeper()
        if front_is_clear():
            move()

def turn_around():
    turn_left()
    turn_left()

def move_to_wall():
    while front_is_clear():
        move()

def collect_one_tower():
    turn_left()
    collect_line_of_beepers()
    turn_around()
    move_to_wall()
    turn_left()

def collect_all_beepers():
    while front_is_clear():
        collect_one_tower()
        move()
    collect_one_tower()

def drop_all_beepers():
    while beepers_in_bag():
        put_beeper()

def return_home():
    turn_around()
    move_to_wall()
    turn_around()

def main():
    """ Karel code goes here! """
    collect_all_beepers()
    drop_all_beepers()
    return_home()

    pass

if __name__ == "__main__":
    run_karel_program(os.path.join(os.getcwd(), 'worlds/karel_10'))