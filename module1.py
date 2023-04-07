#EV3 movement functions
#EV3 code by Maxwell Paradis, Jewel Niekamp, Zach Crozier, Veronica Malusky
import os
import sys
import time
from ev3dev2.sound import Sound
from ev3dev2.motor import Motor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, MediumMotor, SpeedPercent
from ev3dev2.sensor.lego import GyroSensor, OUTPUT_1, OUTPUT_2, OUTPUT_3, OUTPUT_4
from ev3dev2.sensor.lego import ColorSensor, OUTPUT_1, OUTPUT_2, OUTPUT_3, OUTPUT_4

# default set up code DO NOT TOUCH
ON = True
OFF = False

def debug_print(*args, **kwargs):
    '''Print debug messages to stderr.

    This shows up in the output panel in VS Code.
    '''
    print(*args, **kwargs, file=sys.stderr)


def reset_console():
    '''Resets the console to the default state'''
    print('\x1Bc', end='')


def set_cursor(state):
    '''Turn the cursor on or off'''
    if state:
        print('\x1B[?25h', end='')
    else:
        print('\x1B[?25l', end='')


def set_font(name):
    '''Sets the console font

    A full list of fonts can be found with `ls /usr/share/consolefonts`
    '''
    os.system('setfont ' + name)
#End of do not touch section


def forward3ft():
    #setting up the console
    reset_console()
    set_cursor(OFF)

    #designates the motor involved
    motorLeft = Motor(OUTPUT_D)
    motorRight = Motor(OUTPUT_A)

    #makes the motors move
    #speed is 1/4 ft/s
    motorLeft.on(20)
    motorRight.on(20)
    
    #find time for this from veronica also find out the motor speed as well
    time.sleep(12)
    motorLeft.off()
    motorRight.off()

def forward6ft():
    #setting up the console
    reset_console()
    set_cursor(OFF)

    #designates the motor involved
    motorLeft = Motor(OUTPUT_D)
    motorRight = Motor(OUTPUT_A)

    gyro=GyroSensor(OUTPUT_4)

    #setup the gyro
    gyro.reset()

    #makes the motors move
    #speed is 1/2 ft/s
    motorLeft.on(40)
    motorRight.on(40)
    
    #find time for this from veronica also find out the motor speed as well
    time.sleep(12)
    while gyro.angle() >= 0.5:
        time.sleep(.1)
        motorLeft.on(-5)
        motorRight.on(5)

    while gyro.angle() <= 359.5:
        motorLeft.on(5)
        motorRight.on(-5)
        time.sleep(.1)
    motorLeft.off()
    motorRight.off()

def forward9ft():
    #setting up the console
    reset_console()
    set_cursor(OFF)

    #designates the sensors and motor involved
    motorLeft = Motor(OUTPUT_D)
    motorRight = Motor(OUTPUT_A)
    gyro=GyroSensor(OUTPUT_4)

    #setup the gyro
    gyro.reset()

    #makes the motors move
    #speed is 1/4 ft/s
    motorLeft.on(40)
    motorRight.on(40)
    
    #find time for this from veronica also find out the motor speed as well
    time.sleep(18)
    while gyro.angle() >= 0.5:
        time.sleep(.1)
        motorLeft.on(-5)
        motorRight.on(5)

    while gyro.angle() <= 359.5:
        motorLeft.on(5)
        motorRight.on(-5)
        time.sleep(.1)
    motorLeft.off()
    motorRight.off()
    motorLeft.off()
    motorRight.off()

def TurnLeft90():
    #dont touch this part
    reset_console()
    set_cursor(OFF)
    

    #designates the motor and sensors involved
    motorLeft = Motor(OUTPUT_D)
    motorRight = Motor(OUTPUT_A)
    gyro = GyroSensor(OUTPUT_4)

    #setup the gyro
    gyro.reset()




    #makes the motors move
    motorLeft.on(-20)
    motorRight.on(20)
    time.sleep(3.35)
    motorLeft.off()
    motorRight.off()

    # angle checking system
    while gyro.angle() >= 90.5:
        time.sleep(.1)
        motorLeft.on(-5)
        motorRight.on(5)

    while gyro.angle() <= 89.5:
        motorLeft.on(5)
        motorRight.on(-5)
        time.sleep(.1)
    motorLeft.off()
    motorRight.off()
def TurnRight90():
    #dont touch this part
    reset_console()
    set_cursor(OFF)

    #designates the motor involved
    motorLeft = Motor(OUTPUT_D)
    motorRight = Motor(OUTPUT_A)
    gyro = GyroSensor(OUTPUT_4)

    #setup the gyro
    gyro.reset()




    #makes the motors move
    motorLeft.on(20)
    motorRight.on(-20)
    time.sleep(3.35)
    motorLeft.off()
    motorRight.off()

    # angle checking system
    while gyro.angle() >= 270.5:
        time.sleep(.1)
        motorLeft.on(-5)
        motorRight.on(5)

    while gyro.angle() <= 269.5:
        motorLeft.on(5)
        motorRight.on(-5)
        time.sleep(.1)
    motorLeft.off()
    motorRight.off()

def Checkdeg():
    gyro = GyroSensor(OUTPUT_4)
    gyro.reset()
    forward6ft
    degrees = gyro.angle
    print(degrees)

def subtask1():
    reset_console()
    set_cursor(OFF)
    sound = Sound()
    sound.beep()
    #move 36 feet
    forward6ft()
    forward6ft()
    forward6ft()
    forward6ft()
    forward6ft()
    forward6ft()
    TurnRight90()
    #move 84 feet and turn right
    x = 0
    for x in 14:
        forward6ft()
    TurnRight90()
    #move 36 feet
    forward6ft()
    forward6ft()
    forward6ft()
    forward6ft()
    forward6ft()
    forward6ft()
def subtask2():
    reset_console()
    set_cursor(OFF)
    sound = Sound()
    sound.beep()
    #move 12 feet forward then turn left
    forward6ft()
    forward6ft()
    TurnLeft90()
    #move 96 feet
    x = 0
    for x in 14:
        forward6ft()
    #turn left then move 12ft
    TurnLeft90()    
    forward6ft()
    forward6ft()
def barcodeScan(color1, color2, color3, color4):
    #start up section
    reset_console()
    set_cursor(OFF)
    sound = Sound()
    sound.beep()
    #designates the motor involved
    motorLeft = Motor(OUTPUT_D)
    motorRight = Motor(OUTPUT_A)
    gyro = GyroSensor(OUTPUT_4)
    scanner = ColorSensor(OUTPUT_2)

    #setup the gyro and color sensor
    gyro.reset()
    if scanner.color == color1:
        motorLeft.on(20)
        motorRight.on(-20)
        time.sleep(.5)
        if scanner.color == color2:
            motorLeft.on(20)
            motorRight.on(-20)
            time.sleep(.5)
            if scanner.color == color3:
                motorLeft.on(20)
                motorRight.on(-20)
                time.sleep(.5)
                if scanner.color == color4:
                    motorLeft.on(20)
                    motorRight.on(-20)
                    return 1
    return 1
def lift(direction):
    if direction == 1:
        liftmo = MediumMotor(OUTPUT_B)
        liftmo.on(3)
        time.sleep(.5)
    else:
        liftmo = MediumMotor(OUTPUT_B)
        liftmo.on(-3)
        time.sleep(.5)

def main():
    motorLeft = Motor(OUTPUT_D)
    motorRight = Motor(OUTPUT_A)
    gyro = GyroSensor(OUTPUT_4)
    scanner = ColorSensor(OUTPUT_2)
    if (barcodeScan(1,6,1,6) == 1):
        motorLeft.on(20)
        motorRight.on(20)
        time.sleep(.5)
        lift(1)
        time.sleep(.5)
        lift(0)
