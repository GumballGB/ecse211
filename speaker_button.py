#!/usr/bin/env python3

"""
Module to play sounds when the touch sensor is pressed.
This file must be run on the robot.
"""
 
from utils import sound
from utils.brick import TouchSensor, wait_ready_sensors
import time

SOUND = sound.Sound(duration=1.25, pitch="C6", volume=70)
TOUCH_SENSOR = TouchSensor(2)


wait_ready_sensors() # Note: Touch sensors actually have no initialization time


def play_sound():
    "Play a single note."
    SOUND.play()
    SOUND.wait_done()


def play_sound_on_button_press():
    "In an infinite loop, play a single note when the touch sensor is pressed."
    while(True):
        try:
            if(TOUCH_SENSOR.is_pressed()):
                SOUND.play()
                SOUND.wait_done()
        except BaseException:  # capture all exceptions including KeyboardInterrupt (Ctrl-C)
            exit()


if __name__=='__main__':
    play_sound()

    # TODO Implement this function
    play_sound_on_button_press()
