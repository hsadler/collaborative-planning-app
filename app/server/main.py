
import json
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
	static_folder='../client/dist/static',
	template_folder='../client/dist'
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


@socketio.on('create_task')
def create_task(params):
	task_title = params['task_title']
	task = TaskService.create_task(task_title)
	if task is not None:
		task = TaskService.get_task_api_formatted_data(task)
		emit('task_created', task, broadcast=True)


@app.route('/api/get-all-tasks', methods=['GET'])
def get_all_tasks():
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


@app.route('/api/get-task-by-id', methods=['GET'])
def get_task_by_id():
	task_uuid4 = request.args.get('task_id')
	if task_uuid4 is None:
		res = {
			'success': 0,
			'error': '"task_id" param required'
		}
		return make_response(
			jsonify(res),
			400
		)
	task = TaskService.load_task_by_uuid4(task_uuid4)
	if task is not None:
		task = TaskService.get_task_api_formatted_data(task)
	res = {
		'success': 1 if task is not None else 0,
		'task': task
	}
	return jsonify(res)	


########## vote API ##########


@socketio.on('create_or_update_vote')
def create_or_update_vote(params):
	# validate params
	required_params = ['user_id', 'task_id', 'vote_variant']
	for req_param in required_params:
		if req_param not in params:
			return None
	# get params
	user_uuid4 = params['user_id']
	task_uuid4 = params['task_id']
	vote_variant = params['vote_variant']
	# create or update
	vote = VoteService.create_or_update_vote(
		user_uuid4, 
		task_uuid4, 
		vote_variant
	)
	if vote is not None:
		votes = VoteService.load_all_votes_by_task(task_uuid4)
		if votes is not None:
			votes = [
				VoteService.get_vote_api_formatted_data(vote)
				for vote in votes
			]
		emit('refresh_votes', votes, broadcast=True)


@app.route('/api/get-all-votes-by-task', methods=['GET'])
def get_all_votes_by_task():
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


@app.route('/api/get-available-vote-variants', methods=['GET'])
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
	print('connected')
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

