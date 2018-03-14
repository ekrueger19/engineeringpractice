import setup
import RoboPiLib as RPL
import time

now = time.time()
future = now

motorL = 0
motorR = 2

right = 23
front = 16
left = 24

rgo = 2000
lgo = 2000


def Rmin(go):
    future = go + 1
    futureplus = future + 1
    while go < future:
        RPL.servoWrite(motorL, lgo)
        RPL.servoWrite(motorR, rgo)
    while go > future and go < futureplus:
        RPL.servoWrite(motorL, rgo)
        RPL.servoWrite(motorR, rgo)

def Lmin(go):
    future = go + 1
    futureplus = future + 1
    while go < future:
        RPL.servoWrite(motorL, lgo)
        RPL.servoWrite(motorR, rgo)
    while go > future and go < futureplus:
        RPL.servoWrite(motorL, lgo)
        RPL.servoWrite(motorR, lgo)

# next step! add in minimum turning time of ~= 1 second

RPL.servoWrite(motorR, rgo)
RPL.servoWrite(motorR, rgo)
RPL.servoWrite(motorL, lgo)
RPL.servoWrite(motorL, lgo)
while True:
    RPL.servoWrite(motorR, rgo)
    RPL.servoWrite(motorL, lgo)
    print ".............."
    while RPL.digitalRead(front) == 0 and RPL.digitalRead(right) == 0: # reverse
        if RPL.digitalRead(left) == 0:
            RPL.servoWrite(motorR, lgo)
            RPL.servoWrite(motorL, rgo)
    while RPL.digitalRead(front) == 0: # something ahead, turn until nothing
        RPL.servoWrite(motorL, rgo)
        print "++++++"
        now = time.time()
        Rmin(now)
        if RPL.digitalRead(front) != 0: # nothing in front, go
            RPL.servoWrite(motorR, rgo)
            RPL.servoWrite(motorL, lgo)
            print "============="
            break
    while RPL.digitalRead(right) == 0: # something to right...
        print "llllllllllllll"
        RPL.servoWrite(motorL, rgo) # pivot
        now = time.time()
        Rmin(now)
        if RPL.digitalRead(right) != 0: # nothing to side, go
            RPL.servoWrite(motorR, rgo)
            RPL.servoWrite(motorL, lgo)
            print ":::::::::::"
            break
    while RPL.digitalRead(left) == 0: # something to left...
        print "ooooooooooo"
        RPL.servoWrite(motorR, lgo) # pivot
        now = time.time()
        Lmin(now)
        if RPL.digitalRead(right) != 0: # nothing to side, go
            RPL.servoWrite(motorR, rgo)
            RPL.servoWrite(motorL, lgo)
            print "mmmmmmmmmmmmmm"
            break
