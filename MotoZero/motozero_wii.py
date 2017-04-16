#Written by Mari DeGrazia for the Tucson Pi-Bot Wars
#arizona4n6@gmail.com

from gpiozero import Motor, OutputDevice
import time
import cwiid

motor1 = Motor(24,27)
motor1_enable = OutputDevice(5, initial_value=1)
motor2 = Motor(6,22)
motor2_enable = OutputDevice(17, initial_value=1)
motor3 = Motor(23,16)
motor3_enable = OutputDevice(12, initial_value=1)
motor4 = Motor(13,18)
motor4_enable = OutputDevice(25, initial_value=1)

#M1 = Right Front
#M2 = Left Front
#M3 = Left Rear
#M4 = Right Rear

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
#max speed is 1. 
speed = 1

def turnOffMotors():
	motor1.stop()
	motor2.stop()
	motor3.stop()
	motor4.stop()


while True:

	print  wm.state['buttons']
	direction = wm.state['buttons']
	if direction == 256:
		print "Move Backwards"
		motor1.backward(speed)
		motor2.backward(speed)
		motor3.backward(speed)
		motor4.backward(speed)
		time.sleep(.1)
		turnOffMotors()
		
	if direction == 512:
		print "Move Forwards"
		motor1.forward(speed)
		motor2.forward(speed)
		motor3.forward(speed)
		motor4.forward(speed)
		time.sleep(.1)
		turnOffMotors()
		
	if direction == 1024:
		print "Move Right"
		
		
		motor1.forward(.3)
		motor2.forward(speed)
		motor3.forward(speed)
		motor4.forward(.3)
		time.sleep(.1)
		turnOffMotors()

	
	if direction == 2048:
		print "Move Left"
		
		motor1.forward(speed)
		motor2.forward(.3)
		motor3.forward(.3)
		motor4.forward(speed)
		time.sleep(.1)
		turnOffMotors()
	



print "Motor 1, Right Front Forward..."
motor1.forward()
time.sleep(5)
print "Motor 1 Right Front Backward..."
motor1.backward()
time.sleep(5)
motor1.stop()
print "Motor 2 Left Front Forward..."
motor2.forward()
time.sleep(5)
motor2.stop()
print "Motor 2 Left Front Backward..."
motor2.backward()
time.sleep(5)
motor2.stop()
print "Motor 3 Left Rear Forward..."
motor3.forward()
time.sleep(5)
print "Motor 3 Left Read Backward..."
motor3.backward()
time.sleep(5)
motor3.stop()
print "Motor 4 Right Rear Forward..."
motor4.forward()
time.sleep(5)
motor4.stop()
print "Motor 4 Right Rear Backward..."
motor4.backward()
time.sleep(5)
motor1.stop()