import setup
import RoboPiLib as RPL
import time

now = time.time()
future = now

front = 23
front = 16

RPL.servoWrite(0, 2000)
RPL.servoWrite(2, 1000)
print "going original"
while True:
    while RPL.digitalRead(16) == 0:
        while time.time() < future:
            RPL.servoWrite(2, 2000)
            if time.time() >= future:
                RPL.servoWrite(0, 1000)
                RPL.servoWrite(2, 2000)
    while RPL.digitalRead(16) == 1:
        RPL.servoWrite(0, 2000)
        RPL.servoWrite(2, 1000)
        if RPL.digitalRead(16) == 0:
            while time.time() < future:
                RPL.servoWrite(2, 2000)
                if time.time() >= future:
                    RPL.servoWrite(0, 1000)
                    RPL.servoWrite(2, 2000)
