import setup
import RoboPiLib as RPL
import time

now = time.time()
future = now

front = 16
right = 23

# idea: if reading from right and front, turn off left motor
# and vice versa
# problem: doesn't always sense from both sides.

motorL = 2
motorR = 0

# R 1000 is forward
# L 2000 is forward
while True:
    RPL.servoWrite(motorR, 1000)
    RPL.servoWrite(motorL, 2500)
    print "motors on"
    RPL.servoWrite(motorL, 2500)
    future = time.time() + 2
    if RPL.digitalRead(16) == 0: # something ahead or to right, pivot
        future = time.time() + 2
        RPL.servoWrite(motorL, 0)
        RPL.servoWrite(motorR, 0)
        while time.time() < future:
            RPL.servoWrite(motorL, 2500)



# possible problem: sensor not picking up walls
# problem: so far only works on right side
