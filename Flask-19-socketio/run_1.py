from flask import Flask
from flask_sockets import Sockets
import datetime
import time

from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler


app = Flask(__name__)
sockets = Sockets(app)

@sockets.route('/echo1')
class MyWebSocketsHandler(WebSocketHandler):
    def on_connect(self):
        print('on_connect')

    def on_disconnect(self):
        print('on_disconnect')

    def handle_one_request(self):
        print('handle one requirest')

    def on_error(self):
        print('on_error')


@sockets.route('/echo')
def echo_socket(ws):
    while not ws.closed:

        now = datetime.datetime.now().isoformat() + 'Z'
        ws.send(now)
        time.sleep(1)

@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == "__main__":

    server = pywsgi.WSGIServer(('', 8000), app, handler_class=MyWebSocketsHandler)
    print('server start')
    server.serve_forever()