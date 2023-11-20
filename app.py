from flask import Flask, jsonify,request
from flask_socketio import Namespace
from dotenv import load_dotenv
import os
from views.Account import Account
from views.Image import Image
from sockets.message import Message
from flask_socketio import SocketIO

load_dotenv()
app = Flask(__name__)
socketio = SocketIO(app,cors_allowed_origins='*')





@socket.on('message')
def handle_message(message):
    print(message)
    emit('message_received', json.dumps(message))

app.add_url_rule('/account/', view_func = Account.as_view('acc'))
app.add_url_rule('/image/',view_func = Image.as_view('image'))
socketio.on_namespace(Message("/"))

