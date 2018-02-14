#brings in time
import time
#to make sensors work
import setup
import RoboPiLib as RPL
#sensor pin reading
pin = 16
#to make definable in a function
close = RPL.digitalRead(pin)
#which pin the motor is in
motorL = 1
motorR = 2
#motor speeds
x = 1000
y = 2500
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
    fufute = now - 1.5
    #to run motors slower
    RPL.servoWrite(motorL, x - 900)
    RPL.servoWrite(motorR, y - 900)
    #function to stop the motors
    if future > 1.5:
        RPL.servoWrite(motorL, 0)
        RPL.servoWrite(motorR, 0)
        break
