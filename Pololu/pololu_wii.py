#Written by Mari DeGrazia for the Tucson Pi-Bot Wars
#arizona4n6@gmail.com

import cwiid
import time
from pololu_drv8835_rpi import motors, MAX_SPEED

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
motors.setSpeeds(0, 0)
#MAX_SPEED is 480
speed = 300
while True:
	print  wm.state['buttons']
	direction = wm.state['buttons']
	
	if direction == 256:
		#move both motors backward
		print "move backwards"
		motors.motor1.setSpeed(-speed)
		motors.motor2.setSpeed(-speed)
		time.sleep(.1)
		motors.motor1.setSpeed(0)
		motors.motor2.setSpeed(0)

	if direction == 512:
		print "move Forward"
		motors.motor1.setSpeed(speed)
		motors.motor2.setSpeed(speed)
		time.sleep(.1)
		motors.motor1.setSpeed(0)
		motors.motor2.setSpeed(0)
		
	#to make it turn, make one wheel move slower then the other	
	if direction == 1024:
		print "move right"
		motors.motor1.setSpeed(speed-50)
		motors.motor2.setSpeed(speed)
		time.sleep(.1)
		motors.motor1.setSpeed(0)
		motors.motor2.setSpeed(0)

		
	if direction == 2048:
		print "move left"
		motors.motor1.setSpeed(speed)
		motors.motor2.setSpeed(speed-50)
		time.sleep(.1)
		motors.motor1.setSpeed(0)
		motors.motor2.setSpeed(0)

		
		
	
   
