#!/usr/bin/env python3

from time import sleep

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank, OUTPUT_C, OUTPUT_D, MediumMotor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor.lego import UltrasonicSensor


colorleft = ColorSensor(INPUT_1)
colorRight = ColorSensor(INPUT_2)
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
m1 = LargeMotor(OUTPUT_A)

def main():
    while True:
        intensity = colorleft.reflected_light_intensity()
        #tank_drive.on_for_rotations(SpeedPercent(intensity * -1), SpeedPercent(intensity * -1), 10)
        m1.run_forever(intensity)

