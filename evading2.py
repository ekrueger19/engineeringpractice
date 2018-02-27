import setup
import RoboPiLib as RPL
import time

now = time.time()
future = now

front = 23
front = 16

RPL.servoWrite(0, 2000)
RPL.servoWrite(2, 1000)
while True:
    if RPL.digitalRead(16) == 0:
        RPL.servoWrite(0, 0)
        RPL.servoWrite(2, 0)
        print "stopping 1"
        while RPL.digitalRead(16) == 0:
            RPL.servoWrite(2, 2000)
            print "turning 1"
            if RPL.digitalRead(16) != 0:
                RPL.servoWrite(0, 1000)
                RPL.servoWrite(2, 2000)
                break
                print "going 1"


    elif RPL.digitalRead(16) == 1:
        if RPL.digitalRead(23) == 0:
            RPL.servoWrite(0, 0)
            RPL.servoWrite(2, 0)
            print "stopping 1"
            while RPL.digitalRead(23) == 0:
                RPL.servoWrite(2, 2000)
                print "turning 1"
                if RPL.digitalRead(23) != 0:
                    RPL.servoWrite(0, 1000)
                    RPL.servoWrite(2, 2000)
                    break
                    print "going 1"
        elif RPL.digitalRead(23) == 1:
            RPL.servoWrite(0, 1000)
            RPL.servoWrite(2, 2000)
            print "continues 2"
