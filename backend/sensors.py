"""
    Credit for setup given to the following article:

    https://thepihut.com/blogs/raspberry-pi-tutorials/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi
"""

import RPi.GPIO as GPIO
import time

# Setup BCM mode
GPIO.setmode(GPIO.BCM)

# Set pins for HC-SR04
TRIGS = {0, 0, 0}
ECHO = 5

GPIO.setup(ECHO, GPIO.IN)

# Initial setup
for i in range (0, 3):
    GPIO.setup(TRIGS[i], GPIO.OUT)

# Trigger and receive pulse
for i in range(0, 3):
    # Reset trig
    GPIO.output(TRIGS[i], False)

    # Wait .001s and then trigger
    time.sleep(.001)
    GPIO.output(TRIGS[i], True)

    # Wait .00001s then disable trigger
    time.sleep(0.00001)
    GPIO.output(TRIGS[i], False)

    # Set start time while echo input is 0
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    
    # Set end time while echo input is 1
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    # Calculate total pulse duration
    pulse_duration = pulse_end - pulse_start

    # Convert pulse duration to distance in cm
    # 17150 x time = distance ()
    distance = round((pulse_duration * 17150), 2)

GPIO.cleanup()