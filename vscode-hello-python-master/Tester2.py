#!/usr/bin/env python3
import os
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.sensor import INPUT_1, INPUT_3, INPUT_2, INPUT_4
from time import sleep

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, OUTPUT_C, OUTPUT_D, MediumMotor

os.system('setfont Lat15-TerminusBold32x16')

sound = Sound()
counter = 0
sound.beep()



motorLeft = LargeMotor(OUTPUT_A)
motorRight = LargeMotor(OUTPUT_D)
touch = TouchSensor(INPUT_1)
gyro = GyroSensor(INPUT_3)
gyro.calibrate()
sleep(1)

#motorRight.on_for_degrees(50, 1060, True, False)
#motorLeft.on_for_degrees(50, 1060, True, False)

motorLeft.on_for_rotations
buttonpressed = False
while buttonpressed == False:
    motorLeft.on(10)
    motorRight.on(10)
    #print(touch.value())
    motorLeft._position, val = motorLeft.get_attr_int(motorLeft._position, 'position')
    print(val)
    if 359<=val<=361:
        buttonpressed = True

motorLeft.on(0)
motorRight.on(0)
motorLeft._set_brake(True)
motorRight._set_brake(True)



