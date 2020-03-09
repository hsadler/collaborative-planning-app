import uuid

from data_store.mysql_driver import MySqlDriver
from data_struct.vote import Vote


class VoteService():

	"""
	Vote Service. Handles vote related business logic.
	"""

	VOTE_TABLE = 'vote'


	@classmethod
	def create_vote(cls, user_uuid4, task_uuid4, vote_variant):
		vote_uuid4 = uuid.uuid4().hex
		vote = Vote(
			uuid4=vote_uuid4, 
			user_uuid4=user_uuid4, 
			task_uuid4=task_uuid4, 
			variant=vote_variant
		)
		# save to db
		sql = """
			INSERT INTO {0} (uuid4, user_uuid4, task_uuid4, variant) 
			VALUES (:uuid4, :user_uuid4, :task_uuid4, :variant)
		""".format(cls.VOTE_TABLE)
		bind_vars = {
			'uuid4': vote.uuid4,
			'user_uuid4': vote.user_uuid4,
			'task_uuid4': vote.task_uuid4,
			'variant': vote.variant,
		}
		success, query_result = MySqlDriver.query_bind(sql, bind_vars)
		return vote if success else None


	@classmethod
	def create_or_update_vote(cls, user_uuid4, task_uuid4, vote_variant):
		# check for existing vote
		existing_vote = cls.load_vote(user_uuid4, task_uuid4)
		if existing_vote is None:
			# create a new vote
			new_vote = cls.create_vote(
				user_uuid4, 
				task_uuid4, 
				vote_variant
			)
			return new_vote
		else:
			# update existing vote
			updated_vote = cls.update_vote(
				vote=existing_vote, 
				new_vote_variant=vote_variant
			)
			return updated_vote


	@classmethod
	def load_vote(cls, user_uuid4, task_uuid4):
		sql = """
			SELECT * FROM {0} 
			WHERE user_uuid4=:user_uuid4 
			AND task_uuid4=:task_uuid4
		""".format(cls.VOTE_TABLE)
		bind_vars = {
			'user_uuid4': user_uuid4,
			'task_uuid4': task_uuid4
		}
		success, query_result = MySqlDriver.query_bind(sql, bind_vars)
		if success and len(query_result) > 0:
			vote_record = query_result[0]
			return cls.get_vote_struct_from_record(vote_record)
		return None


	@classmethod
	def load_all_votes_by_task(cls, task_uuid4):
		sql = """
			SELECT * FROM {0} 
			WHERE task_uuid4=:task_uuid4
		""".format(cls.VOTE_TABLE)
		bind_vars = {
			'task_uuid4': task_uuid4
		}
		success, query_result = MySqlDriver.query_bind(sql, bind_vars)
		if success and len(query_result) > 0:
			votes = [
				cls.get_vote_struct_from_record(vote_record)
				for vote_record in query_result
			]
			return votes
		return None


	@classmethod
	def update_vote(
		cls, 
		vote,
		new_vote_variant
	):
		# execute db update
		sql = """
			UPDATE {0} 
			SET
				variant=:variant
			WHERE user_uuid4=:user_uuid4
			AND task_uuid4=:task_uuid4
		""".format(cls.VOTE_TABLE)
		bind_vars = {
			'user_uuid4': vote.user_uuid4,
			'task_uuid4': vote.task_uuid4,
			'variant': new_vote_variant
		}
		success, query_result = MySqlDriver.query_bind(sql, bind_vars)
		if success:
			vote.variant = new_vote_variant
			return vote
		return None


	@classmethod
	def get_vote_api_formatted_data(cls, vote):
		return {
			'uuid4': vote.uuid4,
			'user_uuid4': vote.user_uuid4,
			'task_uuid4': vote.task_uuid4,
			'variant': vote.variant
		}

	
	@classmethod
	def get_vote_struct_from_record(cls, vote_record):
		return Vote(
			uuid4=vote_record['uuid4'], 
			user_uuid4=vote_record['user_uuid4'], 
			task_uuid4=vote_record['task_uuid4'], 
			variant=vote_record['variant']
		)

