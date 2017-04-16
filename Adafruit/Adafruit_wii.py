#!/usr/bin/python
#Written by Mari DeGrazia for the Tucson Pi-Bot Wars
#arizona4n6@gmail.com

from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import time
import atexit
import cwiid

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

#connect to the wii remote
print 'Press button 1 + 2 on your Wii Remote...'
time.sleep(1)

wm = None
while not wm:
	try:
		wm=cwiid.Wiimote()
	except:
		print "Still looking for Wii remote..."
		pass


print 'Wii Remote connected...'
time.sleep(1)

Rumble = False
wm.rpt_mode = cwiid.RPT_BTN
#max speed is 255
speed = 200

while True:
	print  wm.state['buttons']
	direction = wm.state['buttons']
	if direction == 256:
		print "Move Backwards"
		myMotor1.setSpeed(speed)
		myMotor1.run(Adafruit_MotorHAT.BACKWARD)
		
		myMotor2.setSpeed(speed)
		myMotor2.run(Adafruit_MotorHAT.BACKWARD)
		
		myMotor3.setSpeed(speed)
		myMotor3.run(Adafruit_MotorHAT.BACKWARD)
		
		myMotor4.setSpeed(speed)
		myMotor4.run(Adafruit_MotorHAT.BACKWARD)
		time.sleep(.1)
		
		turnOffMotors()

	if direction == 512:
		print "Move Forwards"
		myMotor1.setSpeed(speed)
		myMotor1.run(Adafruit_MotorHAT.FORWARD)
		
		myMotor2.setSpeed(speed)
		myMotor2.run(Adafruit_MotorHAT.FORWARD)
		
		myMotor3.setSpeed(speed)
		myMotor3.run(Adafruit_MotorHAT.FORWARD)
		
		myMotor4.setSpeed(speed)
		myMotor4.run(Adafruit_MotorHAT.FORWARD)
		time.sleep(.1)
		
		turnOffMotors()
		
	#to make it turn, make one wheel move slower then the other	
	if direction == 1024:
		print "Move Right"
		myMotor1.setSpeed(speed-100)
		myMotor1.run(Adafruit_MotorHAT.FORWARD)
		
		myMotor2.setSpeed(speed)
		myMotor2.run(Adafruit_MotorHAT.FORWARD)
		
		myMotor3.setSpeed(speed-100)
		myMotor3.run(Adafruit_MotorHAT.FORWARD)
		
		myMotor4.setSpeed(speed)
		myMotor4.run(Adafruit_MotorHAT.FORWARD)
		time.sleep(.1)
		
		turnOffMotors()

	if direction == 2048:
		print "Move Left"
		myMotor1.setSpeed(speed)
		myMotor1.run(Adafruit_MotorHAT.FORWARD)
		
		myMotor2.setSpeed(speed-100)
		myMotor2.run(Adafruit_MotorHAT.FORWARD)
		
		myMotor3.setSpeed(speed)
		myMotor3.run(Adafruit_MotorHAT.FORWARD)
		
		myMotor4.setSpeed(speed-100)
		myMotor4.run(Adafruit_MotorHAT.FORWARD)
		time.sleep(.1)
		
		turnOffMotors()
