import setup
import RoboPiLib as RPL
import time

now = time.time()
future = now

front = 23
front = 16

RPL.servoWrite(0, 1000)
RPL.servoWrite(2, 2000)
while True:
<<<<<<< HEAD
    if RPL.digitalRead(16) == 0:
        RPL.servoWrite(0, 0)
        RPL.servoWrite(2, 0)
        future = time.time() + 2
        print "stopping 1"
=======
    while RPL.digitalRead(16) == 0:
        future = time.time() +2
>>>>>>> 360eb06d151e72c356a7f6b60c4922004ba5181c
        while time.time() < future:
            RPL.servoWrite(2, 2000)
            print "turning 1"
            if time.time() >= future:
                RPL.servoWrite(0, 1000)
                RPL.servoWrite(2, 2000)
                print "going 1"

    elif RPL.digitalRead(16) == 1:
        if RPL.digitalRead(23) == 0:
            future = time.time() + 2
            RPL.servoWrite(0, 0)
            RPL.servoWrite(2, 0)
            print "stopping 2"
            while time.time() < future:
                RPL.servoWrite(2, 2000)
                if time.time() >= future:
                    RPL.servoWrite(0, 1000)
                    RPL.servoWrite(2, 2000)
