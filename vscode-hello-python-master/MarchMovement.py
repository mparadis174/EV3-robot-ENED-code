#!/usr/bin/env python3
import os
import math
from time import sleep
from ev3dev2.sound import Sound
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, OUTPUT_C, OUTPUT_D, MediumMotor, MoveTank
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from ev3dev2 import *
os.system('setfont Lat15-TerminusBold32x16')


"""
This section of code is for initialization of objects
"""

#motorLeft = LargeMotor(OUTPUT_A)
#motorRight = LargeMotor(OUTPUT_D)

tank = MoveTank(OUTPUT_A, OUTPUT_D)



def main():

    tank.on_for_degrees(50, 50, 1080, True, False)


if __name__ == '__main__':
    main()
