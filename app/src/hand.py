from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO


class Hand(object):
    def __init__(self):
        print("New Hand Created!")