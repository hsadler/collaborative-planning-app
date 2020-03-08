
from flask import (
	Flask,
	render_template,
	jsonify
)
from flask_socketio import SocketIO, emit


# init Flask app instance
app = Flask(
	__name__,
	
	# testing    
	template_folder='../client'

	# static_folder='../client/dist/static',
	# template_folder='../client/dist'
)
# init socketio
socketio = SocketIO(app)


# ping route (for testing)
@app.route('/ping', methods=['GET'])
def ping():
	return jsonify({ 'output': 'hi there' })


# TESTING: sockets!
@socketio.on('chat message')
def chat_message(message):
    emit('chat message', message, broadcast=True)

@socketio.on('connect')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')


# serve index for non-API calls
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
	return render_template('index.html')


# run the app if executed as main file to python interpreter
if __name__ == '__main__':
	socketio.run(app, host='0.0.0.0', port=80)


