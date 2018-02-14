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

motorL = 1
motorR = 0

# R 2000 is forward
# L 1000 is forward
RPL.servoWrite(1, 1000)
RPL.servoWrite(0, 2000)
while True:
<<<<<<< HEAD
    RPL.servoWrite(motorR, 1000)
    print "right motor on"
    future = time.time() + 2
=======
>>>>>>> a42355a135e61232383307bb43413b2df2036610
    if RPL.digitalRead(16) == 0 or RPL.digitalRead(23) == 0: # something ahead or to right, pivot
        future = time.time() + 2
        RPL.servoWrite(motorL, 0)
        RPL.servoWrite(motorR, 0)
        while time.time() < future:
            RPL.servoWrite(motorR, 2000)



# possible problem: sensor not picking up walls
# problem: so far only works on right side
