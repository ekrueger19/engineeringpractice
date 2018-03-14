import setup
import RoboPiLib as RPL
import time

now = time.time()
future = now

motorR = 1
motorL = 0
# lsens = 23
# fsens = 16

# motorR forward = 1000
# motorL forward = 2000

while RPL.digitalRead(23) == 0:
  RPL.servoWrite(motorR,2000)
  RPL.servoWrite(motorL,1000)
  if RPL.digitalRead(23) == 1:
    future = time.time() + 2
    RPL.servoWrite(motorR,2000)
    RPL.servoWrite(motorL,0)
    while time.time() < future:
        RPL.servoWrite(motorR, 2000)
