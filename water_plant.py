# water_plant.py uses GPIO 19 and 26 to turn on transistors,
# which turn on the air pump motor to water the plant every
# 1.5 days.
# Xitang - 12/20/2018

# Import GPIO library and time library
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # Set GPIO Pins to be referred in Broadcom SOC channel

# Set up Transistor Control GPIO Pins
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
# Set up LED Debug GPIO Pin
GPIO.setup(13, GPIO.OUT)
# Set up Exit GPIO Pin
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Turn on the air pump motor for 2 seconds to water plant
GPIO.output(19, GPIO.HIGH)
GPIO.output(26, GPIO.HIGH)
time.sleep(2)
GPIO.output(19, GPIO.LOW)
GPIO.output(26, GPIO.LOW)

# Initialize variables
water_interval_sec = 1.5 * 24 * 60 * 60 # 1.5 days
start_time = time.time()
counter = 0

while True:
	# If exit button is pressed, reset used GPIOs as inputs and exit
	if (not GPIO.input(17)):
		GPIO.cleanup()
		print("Exit Program")
		break
	# Water the plant every 1.5 days
	if ((time.time() - start_time) > water_interval_sec):
		start_time = time.time()
		counter = counter + 1
		print (counter)
		GPIO.output(19, GPIO.HIGH)
		GPIO.output(26, GPIO.HIGH)
		time.sleep(2)
		GPIO.output(19, GPIO.LOW)
		GPIO.output(26, GPIO.LOW)
		print ("done")
	# Flash debug LED every 5 seconds
	time.sleep(4)
	GPIO.output(13, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(13, GPIO.LOW)