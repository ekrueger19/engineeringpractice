import setup
import RoboPiLib as RPL
import time

now = time.time()
future = now

# next step! add in minimum turning time of ~= 1 second

motorL = 2
motorR = 0

right = 23
front = 16
left = 17

rgo = 1000
lgo = 2000

RPL.servoWrite(motorR, rgo)
RPL.servoWrite(motorR, rgo)
RPL.servoWrite(motorL, lgo)
RPL.servoWrite(motorL, lgo)
while True:
    RPL.servoWrite(motorR, rgo)
    RPL.servoWrite(motorL, lgo)
    print ".............."
    while RPL.digitalRead(front) == 0 and RPL.digitalRead(right) == 0 and RPL.digitalRead(left) == 0:
        RPL.servoWrite(motorR, lgo)
        RPL.servoWrite(motorL, rgo)
    while RPL.digitalRead(front) == 0: # something ahead, turn until nothing
        RPL.servoWrite(motorL, rgo)
        print "++++++"
        if RPL.digitalRead(front) != 0: # nothing in front, go
            RPL.servoWrite(motorR, rgo)
            RPL.servoWrite(motorL, lgo)
            print "============="
            break
    while RPL.digitalRead(right) == 0: # something to right...
        print "llllllllllllll"
        RPL.servoWrite(motorL, rgo) # pivot
        if RPL.digitalRead(right) != 0: # nothing to side, go
            RPL.servoWrite(motorR, rgo)
            RPL.servoWrite(motorL, lgo)
            print ":::::::::::"
            break
    while RPL.digitalRead(left) == 0: # something to left...
        print "ooooooooooo"
        RPL.servoWrite(motorR, lgo) # pivot
        if RPL.digitalRead(right) != 0: # nothing to side, go
            RPL.servoWrite(motorR, rgo)
            RPL.servoWrite(motorL, lgo)
            print "mmmmmmmmmmmmmm"
            break
