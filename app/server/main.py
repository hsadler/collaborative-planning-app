
from flask import (
	Flask,
	request,
	render_template,
	make_response,
	jsonify
)
from flask_socketio import SocketIO, emit

# import services
from service.user_service import UserService


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



########## user API ##########


# TODO: change to POST, GET is only for testing...
@app.route('/api/create-user', methods=['GET'])
def create_user():
	user_name = request.args.get('user_name')
	if user_name is None:
		return make_response(
			jsonify({'error': '"user_name" param required'}),
			400
		)
	user = UserService.create_user(user_name)
	if user is not None:
		user = UserService.get_user_api_formatted_data(user)
	res = {
		'success': 1 if user is not None else 0,
		'user': user
	}
	return jsonify(res)


@app.route('/api/get-all-users', methods=['GET'])
def get_all_users():
	users = UserService.load_all_users()
	if users is not None:
		users = [
			UserService.get_user_api_formatted_data(user)
			for user in users
		]
	res = {
		'success': 1 if users is not None else 0,
		'users': users
	}
	return jsonify(res)



########## task API ##########


# TODO: change to POST, GET is only for testing...
@app.route('/api/create-task', methods=['GET'])
def create_task():
	task_name = request.args.get('task_name')
	if task_name is None:
		return make_response(
			jsonify({'error': '"task_name" param required'}),
			400
		)
	# TODO: implement stub
	return jsonify({'status': 'endpoint not yet implemented'})


@app.route('/api/get-all-tasks-simple-metadata', methods=['GET'])
def get_all_tasks_simple_metadata():
	# TODO: implement stub
	return jsonify({'status': 'endpoint not yet implemented'})


@app.route('/api/get-task-by-id', methods=['GET'])
def get_task_by_id():
	task_uuid4 = request.args.get('task_id')
	if task_uuid4 is None:
		return make_response(
			jsonify({'error': '"task_id" param required'}),
			400
		)
	# TODO: implement stub
	return jsonify({'status': 'endpoint not yet implemented'})



########## vote API ##########


@app.route('/api/create-or-update-vote', methods=['GET'])
def create_or_update_vote():
	# validate input params
	required_args = ['user_id', 'task_id', 'vote_variant']
	for req_arg in required_args:
		if req_arg not in request.args:
			return make_response(
				jsonify({'error': 'missing required input param'}),
				400
			)
	# TODO: implement stub
	return jsonify({'status': 'endpoint not yet implemented'})


@app.route('/api/get-all-votes-by-task-id', methods=['GET'])
def get_all_votes_by_task_id():
	task_uuid4 = request.args.get('task_id')
	if task_uuid4 is None:
		return make_response(
			jsonify({'error': '"task_id" param required'}),
			400
		)
	# TODO: implement stub
	return jsonify({'status': 'endpoint not yet implemented'})



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
	socketio.run(app, host='0.0.0.0', port=80, debug=True)

