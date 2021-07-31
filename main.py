from flask import Flask
from flask_socketio import SocketIO, send
from flask_user import login_required

# if ImportError:
#     install()

from app import app_

if __name__=="__main__":
    
    socketio.run(app)

# https://github.com/humiaozuzu/awesome-flask#authentication
