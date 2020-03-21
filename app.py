from flask import Flask
import random
import string

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/random')
def generate_random():
    return str(random.randrange(0, 52, 1))


if __name__ == '__main__':
    app.run()
