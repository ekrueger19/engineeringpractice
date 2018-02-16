import setup
import RoboPiLib as RPL
import time

now = time.time()

front = 23
front = 16

RPL.servoWrite(0, 2000)
RPL.servoWrite(2, 1000)
while True:
    if RPL.digitalRead(16) == 0:
        if RPL.digitalRead(23) == 0:
            future = time.time() + 2
            RPL.servoWrite(0, 0)
            RPL.servoWrite(2, 0)
            print "stopping"
            while time.time() < future:
                RPL.servoWrite(0, 2000)
                print "turning"
                if time.time() >= future:
                    RPL.servoWrite(0, 2000)
                    RPL.servoWrite(2, 1000)
                    print "going"
        elif RPL.digitalRead(23) == 1:
            RPL.servoWrite(0, 2000)
            RPL.servoWrite(2, 1000)
            print "going"
    elif RPL.digitalRead(16) == 1:
        if RPL.digitalRead(23) == 0:
            future = time.time() + 2
            RPL.servoWrite(0, 0)
            RPL.servoWrite(2, 0)
            print "stopping"
            while time.time() < future:
                RPL.servoWrite(0, 2000)
                print "turning"
                if time.time() >= future:
                    RPL.servoWrite(0, 2000)
                    RPL.servoWrite(2, 1000)
                    print "going"
        elif RPL.digitalRead(23) == 1:
            RPL.servoWrite(0, 2000)
            RPL.servoWrite(2, 1000)
            print "going"
