#brings in time
import time
#to make sensors work
import setup
import RoboPiLib as RPL

#which pin the motor is in
motorL = 0
motorR = 2
#motor speeds
x = 2000
y = 1000
#it runs when the pin is not reading anything
while RPL.digitalRead(16) == 1:
    #to run motors at regular speed
    RPL.servoWrite(motorL, x)
    RPL.servoWrite(motorR, y)
    if RPL.digitalRead(16) == 0:
        break
#it stops when the sensor senses something
while RPL.digitalRead(16) == 0:
    #so the robot only runs 1.5 seconds
    now = time.time()
    future = time.time() + 0.5
    #to run motors slower
    while time.time() < future:
        RPL.servoWrite(motorL, 1600)
        RPL.servoWrite(motorR, 600)
        #function to stop the motors
        if time.time() >= future:
            RPL.servoWrite(motorL, 0)
            RPL.servoWrite(motorR, 0)
