import serial
import time
import requests

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)

while True:
    data = arduino.readline() 

    if b'play_note' in data:
        data_stringify = data.decode('utf-8')
        data_stringify = data_stringify.strip()

        note = data_stringify.replace("play_note ", "")
        
        # play_note(note)
        url = 'http://127.0.0.1:8001/play/' + note
        requests.get(url)


    time.sleep(1)
