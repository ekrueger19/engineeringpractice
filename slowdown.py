#brings in time
import time
#to make sensors work
import setup
import RoboPiLib as RPL

#to make definable in a function
close = RPL.digitalRead(16)
#which pin the motor is in
motorL = 0
motorR = 2
#motor speeds
x = 2000
y = 1000
#it runs when the pin is not reading anything
while close == 1:
    #to run motors at regular speed
    RPL.servoWrite(motorL, x)
    RPL.servoWrite(motorR, y)
    if close == 0:
        break
#it stops when the sensor senses something
while close == 0:
    #so the robot only runs 1.5 seconds
    now = time.time()
    future = time.time() + 0.5
    #to run motors slower
    while time.time() < future:
        RPL.servoWrite(motorL, x - 400)
        RPL.servoWrite(motorR, y - 400)
        #function to stop the motors
        if time.time() >= future:
            RPL.servoWrite(motorL, 0)
            RPL.servoWrite(motorR, 0)
