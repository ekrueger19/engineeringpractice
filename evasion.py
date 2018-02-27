# Approach a wall obliquely, turn away from it, and proceed.
# 100%: Maintain forward motion while turning away.

import setup
import RoboPiLib as RPL
import time

now = time.time()
future = now

front = 16
right = 23
left = 22

# idea: if reading from right and front, turn off left motor
# and vice versa
# problem: doesn't always sense from both sides.

motorL = 2
motorR = 0

# R 1000 is forward
# L 2500 is forward
while True:
    RPL.servoWrite(motorR, 2000)
    RPL.servoWrite(motorL, 1000)
    future = time.time() + 2
    if RPL.digitalRead(front) == 0: # something ahead, pivot
        future = time.time() + 2
        RPL.servoWrite(motorL, 0)
        RPL.servoWrite(motorR, 0)
        while time.time() < future:
            RPL.servoWrite(motorR, 2000)
    if RPL.digitalRead(right) == 0: # something to right, pivot
        future = time.time() + 2
        RPL.servoWrite(motorL, 0)
        RPL.servoWrite(motorR, 0)
        while time.time() < future:
            RPL.servoWrite(motorR, 2000)
            RPL.servoWrite(motorL, 0)
    if RPL.digitalRead(left) == 0: # something to right, pivot
        future = time.time() + 2
        RPL.servoWrite(motorL, 0)
        RPL.servoWrite(motorR, 0)
        while time.time() < future:
            RPL.servoWrite(motorR, 0)
            RPL.servoWrite(motorL, 2000)

# right now it doesn't work, always just prints 'back it up'
# ideas: split it up, make diff one for right and front, then make clause of the other inside the if



# possible problem: sensor not picking up walls
# problem: so far only works on right side
