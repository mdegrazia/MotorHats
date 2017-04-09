#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

################################# DC motor test!
#M1 = Right Front
#M2 = Left Front
#M3 = Right Rear
#M4 = Left Rear

myMotor1 = mh.getMotor(1)
myMotor2 = mh.getMotor(2)
myMotor3 = mh.getMotor(3)
myMotor4 = mh.getMotor(4)

# set the speed to start, from 0 (off) to 255 (max speed)
myMotor1.setSpeed(255)
myMotor1.run(Adafruit_MotorHAT.FORWARD);
# turn on motor
myMotor1.run(Adafruit_MotorHAT.RELEASE);

myMotor2.setSpeed(255)
myMotor2.run(Adafruit_MotorHAT.FORWARD);
# turn on motor
myMotor2.run(Adafruit_MotorHAT.RELEASE);


myMotor3.setSpeed(255)
myMotor3.run(Adafruit_MotorHAT.FORWARD);
# turn on motor
myMotor3.run(Adafruit_MotorHAT.RELEASE);


myMotor4.setSpeed(255)
myMotor4.run(Adafruit_MotorHAT.FORWARD);
# turn on motor
myMotor4.run(Adafruit_MotorHAT.RELEASE);

print "Right Front Motor 1 Forward"
myMotor1.run(Adafruit_MotorHAT.FORWARD)
time.sleep(5)
myMotor1.run(Adafruit_MotorHAT.RELEASE)

print "Right Front Motor 1 Backward"
myMotor1.run(Adafruit_MotorHAT.BACKWARD)
time.sleep(5)
myMotor1.run(Adafruit_MotorHAT.RELEASE)

print "Left Front Motor 2 Forward"
myMotor2.run(Adafruit_MotorHAT.FORWARD)
time.sleep(5)
myMotor2.run(Adafruit_MotorHAT.RELEASE)

print "Left Front Motor 2 Backward"
myMotor2.run(Adafruit_MotorHAT.BACKWARD)
time.sleep(5)
myMotor2.run(Adafruit_MotorHAT.RELEASE)

print "Right Rear Motor 3 Forward"
myMotor3.run(Adafruit_MotorHAT.FORWARD)
time.sleep(5)
myMotor3.run(Adafruit_MotorHAT.RELEASE)

print "Right Rear Motor 3 Backward"
myMotor3.run(Adafruit_MotorHAT.BACKWARD)
time.sleep(5)
myMotor3.run(Adafruit_MotorHAT.RELEASE);

print "Left Rear Motor 4 Forward"
myMotor4.run(Adafruit_MotorHAT.FORWARD)
time.sleep(5)
myMotor4.run(Adafruit_MotorHAT.RELEASE);

print "Left Rear Motor 4 Backward"
myMotor4.run(Adafruit_MotorHAT.BACKWARD)
time.sleep(5)
myMotor4.run(Adafruit_MotorHAT.RELEASE);