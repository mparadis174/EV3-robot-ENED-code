#EV3 movement functions
#EV3 code by Maxwell Paradis, Jewel Niekamp, Zach Crozier, Veronica Malusky
import os
import sys
import time
from ev3dev2.sound import Sound
from ev3dev2.motor import Motor, LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, MediumMotor, SpeedPercent

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
    sound = Sound()
    sound.beep()

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
    sound = Sound()
    sound.beep()

    #designates the motor involved
    motorLeft = Motor(OUTPUT_D)
    motorRight = Motor(OUTPUT_A)

    #makes the motors move
    #speed is 1/4 ft/s
    motorLeft.on(20)
    motorRight.on(20)
    
    #find time for this from veronica also find out the motor speed as well
    time.sleep(24)
    motorLeft.off()
    motorRight.off()

def TurnLeft90():
    #
    reset_console()
    set_cursor(OFF)
    sound = Sound()
    sound.beep()

    #designates the motor involved
    motorLeft = Motor(OUTPUT_D)
    motorRight = Motor(OUTPUT_A)

    #makes the motors move
    motorLeft.on(-20)
    motorRight.on(20)
    
    #find time for this from veronica also find out the motor speed as well
    time.sleep()
    
