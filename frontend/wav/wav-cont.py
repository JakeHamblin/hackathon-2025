# Using flask to make an api 
# import necessary libraries and functions 
from flask import Flask, jsonify, request 
import json
import playsound
import pygame
from time import sleep


# creating a Flask app 
app = Flask(__name__) 

config = ''

with open('./config.json', 'r') as fin:
    data = fin.read()
    config = json.loads(data)

pygame.init()
sound = pygame.mixer.Sound('fortnite-downed.wav')

# app.config['DEBUG'] = True
# on the terminal type: curl http://127.0.0.1:5000/ 
# returns hello world when we use GET. 
# returns the data that we send when we use POST. 
# @app.route('/', methods = ['GET', 'POST']) 
# def home(): 
#     if(request.method == 'GET'): 
  
#         data = "hello world"
#         return jsonify({'data': data}) 

@app.route('/update_config', methods=['POST'])
def update_conf():
    data = request.get_json()

    with open('./config.json', 'w') as f:
        f.write(json.dumps(data))

    return jsonify({'status': 200})

def play_note(note):
    sound.play()
  
  
# driver function 
if __name__ == '__main__': 
  
    # app.config['ENV'] = 'production'
    # app.run(debug=False, port=8001) 

    while True:
        play_note(0)
        sleep(.2)
