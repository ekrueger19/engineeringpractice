#brings in time
import time
start = time.time()
#to make sensors work
import setup
import RoboPiLib as RPL
#sensor pin reading
pin = raw_input("What is the pin number?")
#to make definable in a function
close = RPL.digitalRead(pin)
#which pin the motor is in
motorL = 1
mororR = 0
x = 1000
y = 2500
#it runs when the pin is not reading anything
while close == 1:
    RPL.servoWrite(mororL, x)
    RPL.servoWrite(motorR, y)
    if close == 0:
        break
#it stops when the sensor senses something
while close == 0:

#to run motors
    RPL.servoWrite(mororL, 100)
    RPL.servoWrite(motorR, 1600)
    if close == 1:
        break
#write code to slow down robot
end = time.time()
