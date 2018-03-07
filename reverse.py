#If all three sensors are 0, stop then back up then turn 90 degrees then go
import setup
import RoboPiLib as RPL
import time

now = time.time()
future = now

while RPL.digitalRead(16) == 1: # nothing in front
    RPL.servoWrite(0, 2000)
    RPL.servoWrite(2, 1000)
    while RPL.digitalRead(16) == 0: # something in front
        while RPL.digitalRead(23) == 0: # something to right
            while RPL.digitalRead(17) == 0: # something to left
                RPL.servoWrite(0, 1000) # motors reverse
                RPL.servoWrite(2, 2000)
                while RPL.digitalRead(16) == 1: # nothing in front
                    while RPL.digitalRead(23) == 1: # nothing to right
                        future = time.time() + 2
                        while time.time() < future:
                            RPL.servoWrite(0, 0)
                            RPL.servoWrite(2, 2000) # motor off
                            if time.time() >= future:
                                RPL.servoWrite(0, 2000)
                                RPL.servoWrite(2, 1000)
                    while RPL.digitalRead(23) == 0:
                        while RPL.digitalRead(17) == 1:
                            future = time.time() + 2
                            while time.time() < future:
                                RPL.servoWrite(0, 2000)
                                RPL.servoWrite(2, 0)
                                if time.time() >= future:
                                    RPL.servoWrite(0, 2000)
                                    RPL.servoWrite(2, 1000)
while RPL.digitalRead(16) == 0:
    while RPL.digitalRead(23) == 0:
        while RPL.digitalRead(17) == 0:
            RPL.servoWrite(0, 2000)
            RPL.servoWrite(2, 1000)
            while RPL.digitalRead(16) == 1:
                while RPL.digitalRead(23) == 1:
                    future = time.time() + 2
                    while time.time() < future:
                        RPL.servoWrite(0, 0)
                        RPL.servoWrite(2, 1000)
                        if time.time() >= future:
                            RPL.servoWrite(0, 2000)
                            RPL.servoWrite(2, 1000)
                while RPL.digitalRead(23) == 0:
                    while RPL.digitalRead(17) == 1:
                        future = time.time() + 2
                        while time.time() < future:
                            RPL.servoWrite(2, 0)
                            RPL.servoWrite(0, 2000)
                            if time.time() >= future:
                                RPL.servoWrite(0, 2000)
                                RPL.servoWrite(2, 1000)
