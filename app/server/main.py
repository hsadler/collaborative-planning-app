
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
from service.task_service import TaskService
from service.vote_service import VoteService
from service.vote_variant_service import VoteVariantService


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


# TODO: convert this to a POST later
@app.route('/api/create-user', methods=['GET'])
def create_user():
	user_name = request.args.get('user_name')
	if user_name is None:
		res = {
			'success': 0,
			'error': '"user_name" param required'
		}
		return make_response(
			jsonify(res),
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


# TODO: convert this to a POST later
@app.route('/api/create-task', methods=['GET'])
def create_task():
	task_title = request.args.get('task_title')
	if task_title is None:
		res = {
			'success': 0,
			'error': '"task_title" param required'
		}
		return make_response(
			jsonify(res),
			400
		)
	task = TaskService.create_task(task_title)
	if task is not None:
		task = TaskService.get_task_api_formatted_data(task)
	res = {
		'success': 1 if task is not None else 0,
		'task': task
	}
	return jsonify(res)


@app.route('/api/get-all-tasks-simple-metadata', methods=['GET'])
def get_all_tasks_simple_metadata():
	tasks = TaskService.load_all_tasks()
	if tasks is not None:
		tasks = [
			TaskService.get_task_api_formatted_data(task)
			for task in tasks
		]
	res = {
		'success': 1 if tasks is not None else 0,
		'tasks': tasks
	}
	return jsonify(res)


# TODO: implement later after making a decision about tying votes to a task
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


# TODO: convert this to socket endpoint later
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
	# get params
	user_uuid4 = request.args.get('user_id')
	task_uuid4 = request.args.get('task_id')
	vote_variant = request.args.get('vote_variant')
	# create or update
	vote = VoteService.create_or_update_vote(
		user_uuid4, 
		task_uuid4, 
		vote_variant
	)
	if vote is not None:
		vote = VoteService.get_vote_api_formatted_data(vote)
	res = {
		'success': 1 if votes is not None else 0,
		'vote': vote
	}
	return jsonify(vote)


@app.route('/api/get-all-votes-by-task-id', methods=['GET'])
def get_all_votes_by_task_id():
	task_uuid4 = request.args.get('task_id')
	if task_uuid4 is None:
		return make_response(
			jsonify({'error': '"task_id" param required'}),
			400
		)
	votes = VoteService.load_all_votes_by_task(task_uuid4)
	if votes is not None:
		votes = [
			VoteService.get_vote_api_formatted_data(vote)
			for vote in votes
		]
	res = {
		'success': 1 if votes is not None else 0,
		'votes': votes
	}
	return jsonify(res)



########## vote-variant API ##########


@app.route('/api/get-all-vote-variants', methods=['GET'])
def get_all_vote_variants():
	vote_variants = VoteVariantService.load_all_vote_variants()
	if vote_variants is not None:
		vote_variants = [
			VoteVariantService.get_vote_variant_api_formatted_data(vote_variant)
			for vote_variant in vote_variants
		]
	res = {
		'success': 1 if vote_variants is not None else 0,
		'vote_variants': vote_variants
	}
	return jsonify(res)



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

