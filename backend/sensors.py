"""
    Credit for setup given to the following article:

    https://thepihut.com/blogs/raspberry-pi-tutorials/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi
"""

import RPi.GPIO as GPIO
import time

try:
    # Setup BCM mode
    GPIO.setmode(GPIO.BOARD)

    # Set pins for HC-SR04
    TRIGS = [7]
    ECHO = 11

    GPIO.setup(ECHO, GPIO.IN)

    # Initial setup
    for i in range (0, 1):
        GPIO.setup(TRIGS[i], GPIO.OUT)

    # Trigger and receive pulse
    for i in range(0, 1):
        GPIO.output(TRIGS[i], GPIO.LOW)

        print("Waiting for sensor to settle")

        time.sleep(.5)

        print("Calculating distance")

        GPIO.output(TRIGS[i], GPIO.HIGH)

        time.sleep(0.00001)

        GPIO.output(TRIGS[i], GPIO.LOW)

        while GPIO.input(ECHO)==0:
                pulse_start_time = time.time()
        while GPIO.input(ECHO)==1:
                pulse_end_time = time.time()

        pulse_duration = pulse_end_time - pulse_start_time
        distance = round(pulse_duration * 17150, 2)
        
        if distance < 50:
            print(f"Play note {i}")

finally:
      GPIO.cleanup()

