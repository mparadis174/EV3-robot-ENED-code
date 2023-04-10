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


#!/usr/bin/env python3
from ev3dev2.motor import *
from time import sleep
from ev3dev2.sensor.lego import *
from ev3dev2.sensor import *
from ev3dev2.display import *
mt = MoveTank(OUTPUT_A,OUTPUT_D)
i = 0
Dist1 = 17 # Input Distance for Box Location
Dist2 = Dist1 - 38 # Distance to Drop-off Location
cs1 = ColorSensor(INPUT_4)
mm = MediumMotor(OUTPUT_B)
bc = []
P1 = [0,1,1,1]
gy = GyroSensor(INPUT_3)
mm.on_for_seconds(60,1.7)
gy.MODE_GYRO_ANG
gy.reset()
screen = Display()
dot = 0
dot2 = 20
mt.on_for_rotations(SpeedRPM(-40),SpeedRPM(-40),((Dist1-0.6)/8.2))
cs1.MODE_COL_REFLECT
for i in range(4):
    if cs1.reflected_light_intensity > 20:
       bc.append(1)                      # 1 is white
    else:
       bc.append(0)                      # 0 is black
    mt.on_for_rotations(SpeedRPM(5),SpeedRPM(5),(0.52/8.4),True,True)
    sleep(2)
for j in range(4):
    dot = dot + 20
    dot2 = dot2 + 20
    if bc[j] == 1:
        screen.rectangle(False, x1=dot, y1=20, x2=dot2, y2=60, fill_color='white')
    else:
        screen.rectangle(False, x1=dot, y1=20, x2=dot2, y2=60, fill_color='black')
    screen.update()
if bc == P1:
    screen.text_pixels('Barcode Matches',False,20,80,'black')
else:
    screen.text_pixels('Barcode Does Not Match',False,20,80,'black')
screen.update()

sleep(10)
gy.reset()
mt.on_for_rotations(SpeedRPM(20),SpeedRPM(20),0.80)
mt.on_for_rotations(SpeedRPM(-12),SpeedRPM(-20),2)
while gy.angle < 83:
    mt.on(-10,10)
gy.reset()
mt.on_for_rotations(SpeedRPM(-50),SpeedRPM(-50),0.2)
mm.on_for_seconds(-60,1.6)
mt.on_for_rotations(SpeedRPM(50),SpeedRPM(50),1)
while gy.angle>-55:
    mt.on(10,-10)
mt.on_for_rotations(SpeedRPM(-50),SpeedRPM(-50),(19/8.2))
