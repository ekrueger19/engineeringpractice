# Approach a wall obliquely, turn away from it, and proceed.
# 100%: Maintain forward motion while turning away.

import setup
import RoboPiLib as RPL
import time

now = time.time()
future = now

front = 16
right = 23

motorL = 0
motorR = 2

# R 2000 is forward
# L 1000 is forward

while True:
    RPL.servoWrite(motorR, 2000)
    RPL.servoWrite(motorL, 1000)
    if RPL.digitalRead(front) == 0 and RPL.digitalRead(right) == 0:
        while RPL.digitalRead(front) == 0 and RPL.digitalRead(right) == 0:
            RPL.servoWrite(motorL, 2000)
            RPL.servoWrite(motorR, 1000)
            print "back it up"
    elif RPL.digitalRead(front) == 0 or RPL.digitalRead(right) == 0: # something ahead or to right, pivot
        future = time.time() + 1
        RPL.servoWrite(motorL, 0)
        while time.time() > future:
            RPL.servoWrite(motorL, 2000)
            print "SPIN"

# right now it doesn't work, always just prints 'back it up'
# ideas: split it up, make diff one for right and front, then make clause of the other inside the if



# possible problem: sensor not picking up walls
# problem: so far only works on right side
