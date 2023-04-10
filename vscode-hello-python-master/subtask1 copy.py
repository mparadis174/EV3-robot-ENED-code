#!/usr/bin/env python3
import os
import math
from time import sleep
from ev3dev2.sound import Sound
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, OUTPUT_C, OUTPUT_D, MediumMotor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from ev3dev2 import *
os.system('setfont Lat15-TerminusBold32x16')

#GLOBAL VARIABLES
WAIT_RUNNING_TIMEOUT = 100
WHEEL_RAD = 3.44 #cm
DRIVE_DIST_CONST = 1.0005

#FUNCTIONS____________________________________________________________________

def motor_stop():
    motorLeft.on(0)
    motorRight.on(0)

##END FUNCTION______________________________________________________________________

def drive_to_distance(dist, speed, block = False):   #IN CENTIMETERS
    #Distance / Circumferance * 360 to get degrees of rotation
    targetDeg = ((dist / (2 * math.pi * WHEEL_RAD)) * 360) * DRIVE_DIST_CONST

    leftboost = 0
    rightboost = 0
    gyroRel = gyro.value()

    encodeLeftStart = motorLeft.get_attr_int(motorLeft._position, 'position')
    encodeRightStart = motorRight.get_attr_int(motorRight._position, 'position')


    if dist > 0:
        while True:
            gyroVal = gyro.value()

            if gyroVal < 0:
                leftboost = abs(gyroVal - gyroRel)
            else:
                leftboost = 0

            if gyroVal > 0:
                rightboost = abs(gyroVal - gyroRel)
            else:
                rightboost = 0

            motorLeft.on(speed + (leftboost/2))
            motorRight.on(speed + (rightboost/2))

            #encodeLeft = motorLeft.get_attr_int(motorLeft._position, 'position')
            #encodeRight = motorRight.get_attr_int(motorRight._position, 'position')
            #encodeAvg = (encodeLeft[1] + encodeRight[1]) / 2
            #print(encodeAvg)
            #print(targetDeg)

            encodeLeft = motorLeft.get_attr_int(motorLeft._position, 'position')
            encodeRight = motorRight.get_attr_int(motorRight._position, 'position')

            encodeRevLeft = encodeLeft[1] - encodeLeftStart[1]
            encodeRevRight = encodeRight[1] - encodeRightStart[1]
            encodeAvg = (encodeRevLeft + encodeRevRight) / 2

            if encodeAvg >= (targetDeg):
                break
        motor_stop()

    if dist < 0:
        while True:
            gyroVal = gyro.value()

            if gyroVal < 0:
                leftboost = abs(gyroVal - gyroRel)
            else:
                leftboost = 0

            if gyroVal > 0:
                rightboost = abs(gyroVal - gyroRel)
            else:
                rightboost = 0

            motorLeft.on(speed + (leftboost/2))
            motorRight.on(speed + (rightboost/2))

            encodeLeft = motorLeft.get_attr_int(motorLeft._position, 'position')
            encodeRight = motorRight.get_attr_int(motorRight._position, 'position')

            encodeRevLeft = encodeLeft[1] - encodeLeftStart[1]
            encodeRevRight = encodeRight[1] - encodeRightStart[1]
            encodeAvg = (encodeRevLeft + encodeRevRight) / 2
            #print(encodeAvg)
            #print(targetDeg)

            if encodeAvg <= (targetDeg):
                break
        motor_stop()



##END FUNCTION_______________________________________________________

def turn_on_point(angle, speed):

    gyroTarget = gyro.value() + angle
    turnDir = ""

    if angle > 0 :
        turnDir = 'right'
    else:
        turnDir = 'left'

    if turnDir == "right":
        motorLeftSpeed = speed
        motorRightSpeed = -speed
        while True:
            motorLeft.on(motorLeftSpeed)
            motorRight.on(motorRightSpeed)
            if gyro.value() + 2 > gyroTarget:
                break
    motor_stop()

    if turnDir == "left":
        motorLeftSpeed = -speed
        motorRightSpeed = speed
        while True:
            motorLeft.on(motorLeftSpeed)
            motorRight.on(motorRightSpeed)
            if gyro.value() - 2 < gyroTarget:
                break
        motor_stop()


##END FUNCTION_____________________________________________________________


def calc_parabola_vertex(x1, y1, x2, y2, x3, y3):
		denom = (x1-x2) * (x1-x3) * (x2-x3);
		A     = (x3 * (y2-y1) + x2 * (y1-y3) + x1 * (y3-y2)) / denom;
		B     = (x3*x3 * (y1-y2) + x2*x2 * (y3-y1) + x1*x1 * (y2-y3)) / denom;
		C     = (x2 * x3 * (x2-x3) * y1+x3 * x1 * (x3-x1) * y2+x1 * x2 * (x1-x2) * y3) / denom;

		return A,B,C

def newStraightLine(dist, speed, block = False):
    targetDeg = ((dist / (2 * math.pi * WHEEL_RAD)) * 360) * DRIVE_DIST_CONST
    startspeed = speed/3

    x1, y1 = (0, startspeed)  #Start of movement
    x2, y2 = (targetDeg/2, speed)   #middle of movement
    x3, y3 = (targetDeg, startspeed)   # end of movement

    A, B, C = calc_parabola_vertex(x1, y1, x2, y2, x3, y3)

    currentspeed =0

def barcodeRead(side):
    barcodeList = []
    # 0 is what, 1 is black
    dist = 0.5
    speed = 20


    if side == "left":

        for i in range(4):

            if leftC.value() > 20:
                barcodeList.append(0)
            else:
                barcodeList.append(1)

            drive_to_distance(dist, speed)

    if side == "right":

          for i in range(4):

            if rightC.value() > 20:
                barcodeList.append(0)
            else:
                barcodeList.append(1)

            drive_to_distance(dist, speed)

    return barcodeList





#INITIALIZATION OF MOTORS AND SENSORS. STARTUP TASKS
sound = Sound()
sound.beep()

motorLeft = LargeMotor(OUTPUT_A)
motorRight = LargeMotor(OUTPUT_D)
lift = MediumMotor(OUTPUT_C)
gyro = GyroSensor(INPUT_3)
leftC = ColorSensor(INPUT_1)
rightC = ColorSensor(INPUT_4)
ultra = UltrasonicSensor(INPUT_2)


gyro.calibrate()
leftC.MODE_COL_REFLECT
rightC.MODE_COL_REFLECT
sleep(0.5)

sound.beep()

#shelf name, xcoord, ycoord     these coords are for the bottom left of the shelf
shelfList = [['a1', 6, 18],
             ['a2', 6, 42],
             ['c1', 6, 66],
             ['c2', 6, 90],
             ['b1', 66, 18],
             ['b2', 66, 42],
             ['d1', 66, 66],
             ['d2', 66, 90]]

#box number, xcoord, ycoord. coordinates are relative to the the bootom left of the shelf.
boxList = [[1, 3, -3],
           [2, 9, -3],
           [3, 15, -3],
           [4, 21, -3],
           [5, 27, -3],
           [6, 33, -3],
           [7, 3, 15],
           [8, 9, 15],
           [9, 15, 15],
           [10, 21, 15],
           [11, 27, 15],
           [12, 33, 15]]


#$$$$$$$$    MAIN SCRIPTING. PUT PROGRAMMING HERE @LAILANI @JULIA
def main():
    while True:
       # leftC._ensure_mode(leftC.MODE_COL_COLOR)

        print(leftC.value(0), rightC.value(0))




#_______________________DO NOT TOUCH_______________________________
if __name__ == '__main__':
    main()
