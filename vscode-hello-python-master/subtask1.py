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





#INITIALIZATION OF MOTORS AND SENSORS. STARTUP TASKS
sound = Sound()
sound.beep()

motorLeft = LargeMotor(OUTPUT_A)
motorRight = LargeMotor(OUTPUT_D)
Lift = MediumMotor(OUTPUT_C)
gyro = GyroSensor(INPUT_3)
#touch = TouchSensor(INPUT_1)
gyro.calibrate()
sleep(0.5)

sound.beep()


#$$$$$$$$    MAIN SCRIPTING. PUT PROGRAMMING HERE @LAILANI @JULIA
def main():
    a = True
    b = True  # cHANGE THIS FOR WHAT TASK IS NEEDED. TRUE MEANS THAT IT WILL RUN.

    if a == False:

        laps = 4 # HOW MANY LAPS YOU WANT
        count =0
        #motorLeft.on(20)
        while count < laps:
            drive_to_distance(100, 30)   #dISTANCE
            sleep(0.5)
            turn_on_point(180, 5)
            sleep(0.5)
            drive_to_distance(100,30)  # DISTANCE
            sleep(0.5)
            turn_on_point(-180, 5)
            sleep(0.5)
            count+=1
            #while True:
            #    encodeLeft = motorLeft.get_attr_int(motorLeft._position, 'position')
            #    encodeRight = motorRight.get_attr_int(motorRight._position, 'position')
            #    print(encodeLeft[1])

    if b == False:
        laps = 4  # HOW MANY LAPS YOU WANT
        count =0
        #motorLeft.on(20)
        while count < laps:
            drive_to_distance(30, 30)  # dISTANCE IN CENTIMETERS
            sleep(0.5)
            drive_to_distance(-30, -30) #IT NEEDS TO MOVE BACKWARD. USE NEGATIVE DISTANCE
            sleep(0.5)
            count += 1


#_______________________DO NOT TOUCH_______________________________
if __name__ == '__main__':
    main()
