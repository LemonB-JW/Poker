from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO
import random
import string


class Game(object):
    def __init__(self, size):
        self.game_id = 1
        self.players = []
        self.size = size

    @classmethod
    def generate_room_id(cls):
        return random.randrange(0, 100, 1)

    def to_json(self):
        return {
            "game_id": self.game_id,
            "players": self.players,
            "size": self.size
        }
