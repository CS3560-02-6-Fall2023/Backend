from flask import Flask, jsonify,request
from flask_socketio import SocketIO, emit
from dotenv import load_dotenv
import os
from views.Account import Account
from views.Image import Image
from flask_cors import CORS


load_dotenv()
app = Flask(__name__)
socket = SocketIO(app,logger=True, engineio_logger=True)
CORS(app)


@socket.on('connect')
def test_connect():
    emit('after connect',  {'data':'Lets dance'})


app.add_url_rule('/account/', view_func = Account.as_view('acc'))
app.add_url_rule('/image/',view_func = Image.as_view('image'))