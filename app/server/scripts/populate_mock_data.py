import uuid
import random
import sys
sys.path.append('..')

from data_store.mysql_driver import MySqlDriver
from service.user_service import UserService
from service.task_service import TaskService
from service.vote_service import VoteService
from service.vote_variant_service import VoteVariantService
from utils.print import ppp


# mock data
user_names = ['jim', 'bob', 'sara', 'penny']
task_titles = ['do the dishes', 'buy a car', 'build an app']


# populate mock users
users = []
for user_name in user_names:
	users.append(UserService.create_user(user_name))

# populate mock tasks
tasks = []
for title in task_titles:
	tasks.append(TaskService.create_task(title))

# load vote variants for reference
vote_variants = VoteVariantService.load_all_vote_variants()

# populate mock votes
for user in users:
	for task in tasks:
		VoteService.create_vote(
			user.uuid4, 
			task.uuid4, 
			random.choice(vote_variants).variant
		)

