#Written by Mari DeGrazia for the Tucson Pi-Bot Wars
#arizona4n6@gmail.com

from gpiozero import Motor, OutputDevice
import time

motor1 = Motor(24,27)
motor1_enable = OutputDevice(5, initial_value=1)
motor2 = Motor(6,22)
motor2_enable = OutputDevice(17, initial_value=1)
motor3 = Motor(23,16)
motor3_enable = OutputDevice(12, initial_value=1)
motor4 = Motor(13,18)
motor4_enable = OutputDevice(25, initial_value=1)


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