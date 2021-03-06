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
    while RPL.digitalRead(16) == 0:
        RPL.servoWrite(0, 0)
        RPL.servoWrite(2, 0)
        future = time.time() + 2
        while time.time() < future:
            RPL.servoWrite(2, 2000)
            if time.time() >= future:
                RPL.servoWrite(0, 1000)
                RPL.servoWrite(2, 2000)
    while RPL.digitalRead(16) == 1:
        if RPL.digitalRead(23) == 0:
            future = time.time() + 2
            while time.time() < future:
                RPL.servoWrite(2, 2000)
                if time.time() >= future:
                    RPL.servoWrite(0, 1000)
                    RPL.servoWrite(2, 2000)
        elif RPL.digitalRead(23) == 1:
            RPL.servoWrite(0, 1000)
            RPL.servoWrite(2, 2000)
