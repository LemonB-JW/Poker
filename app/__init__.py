from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, join_room, leave_room, send, emit
from src.game import Game
from src.hand import Hand
from src.player import Player
import random
import string

app = Flask(__name__)
socketio = SocketIO(app)
ROOMS = {}

@app.route('/')
def hello_world():
    return render_template('testSocket.html')


@app.route('/random')
def generate_random():
    return str(random.randrange(0, 52, 1))


@socketio.on('create')
def on_create(data):
    gm = Game(5)
    room = gm.game_id
    ROOMS[room] = gm
    join_room(room)
    emit('join_room', {'room': room})

    print(gm.game_id)
    return gm.game_id


@socketio.on('join_room')
def on_join(data):
    room = data['room']
    if room in ROOMS:
        join_room(room)
        send(ROOMS[room].to_json(), room=room)
        print(ROOMS)
    else:
        emit('error', {'error': 'Unable to join room. Room does not exist'})


# @socketio.on('push')
# def on_push(data):
#     msg = data['msg']
#     send(msg, room=room)
#      print(msg)


if __name__ == '__main__':
    app.run()
