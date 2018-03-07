import setup
import RoboPiLib as RPL
import time

now = time.time()
future = now

motorR = 2
motorL = 1
# motorR forward = 1000
# motorL forward = 2000

while RPL.digitalRead(23) == 1:
  RPL.servoWrite(motorR,1000)
  RPL.servoWrite(motorL,2000)
  if RPL.digitalRead(23) == 0:
    future = time.time() + 2
    RPL.servoWrite(motorR,1000)
    RPL.servoWrite(motorL,0)
    while time.time() < future:
        RPL.servoWrite(motorR, 1000)
