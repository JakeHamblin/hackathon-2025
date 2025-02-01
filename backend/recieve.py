import serial
import time

arduino = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=.1)

while True:
    data = arduino.readline() 

    if b'play_note' in data:
        data_stringify = data.decode('utf-8')
        data_stringify = data_stringify.strip()

        note = data_stringify.replace("play ", "")

        # play_note(note)

    time.sleep(1)