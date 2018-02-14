import setup
import RoboPiLib as RPL
start = raw_input("y/n?")
if start == y:
    RPL.servoWrite(1, 2000)
elif start == n:
    RPL.servoWrite(1, 0)
