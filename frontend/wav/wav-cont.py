# Using flask to make an api 
# import necessary libraries and functions 
from flask import Flask, jsonify, request 
import json
import pygame
from time import sleep


# creating a Flask app 
app = Flask(__name__) 

config = ''

with open('./config.json', 'r') as fin:
    data = fin.read()
    config = json.loads(data)

pygame.init()

sounds = []
for f in config['notes']:
    sound_module = pygame.mixer.Sound(f)
    sounds.append(sound_module)

# sound = pygame.mixer.Sound('fortnite-downed.wav')

@app.route('/update_config', methods=['POST'])
def update_conf():
    data = request.get_json()

    with open('./config.json', 'w') as f:
        f.write(json.dumps(data))

    return jsonify({'status': 200})

@app.route('/play/<int:note>', methods=['GET'])
def please(note):
    play_note(note)

    return jsonify({'status': 200})

def play_note(note):
    sounds[note].play()
  
  
# driver function 
if __name__ == '__main__': 
  
    app.config['ENV'] = 'production'
    app.run(debug=False, port=8001) 


