from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO
import random
import string


class Player(object):
    def __init__(self):
        self.player_id = self.generate_room_id()
