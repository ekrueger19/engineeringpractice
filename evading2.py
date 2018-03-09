import setup
import RoboPiLib as RPL
import time

now = time.time()
future = now

motorL = 2
motorR = 0

right = 23
front = 16


RPL.servoWrite(motorR, 1000)
RPL.servoWrite(motorR, 1000)
RPL.servoWrite(motorL, 2000)
RPL.servoWrite(motorL, 2000)
while True:
    RPL.servoWrite(motorR, 1000)
    RPL.servoWrite(motorL, 2000)
    print ".............."
    while RPL.digitalRead(front) == 0: # ... turn until nothing
        RPL.servoWrite(motorL, 1000)
        print "++++++"
        if RPL.digitalRead(front) != 0: # nothing in front, go
            RPL.servoWrite(motorR, 1000)
            RPL.servoWrite(motorL, 2000)
            print "============="
            break
    while RPL.digitalRead(right) == 0: # something to right...
        print "llllllllllllll"
        RPL.servoWrite(motorL, 2000)
        if RPL.digitalRead(right) != 0: # nothing to side, go
            RPL.servoWrite(motorR, 1000)
            RPL.servoWrite(motorL, 2000)
            print ":::::::::::"
            break
