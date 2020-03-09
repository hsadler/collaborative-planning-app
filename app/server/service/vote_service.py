

class VoteService():

	"""
	Vote Service. Handles vote related business logic.
	"""

	VOTE_TABLE = 'vote'


	# TODO: implement stubs


	@classmethod
	def create_vote(cls, user_uuid4, task_uuid4, vote_variant):
		# stub
		pass


	@classmethod
	def create_or_update_vote(cls, user_uuid4, task_uuid4, vote_variant):
		# stub
		pass


	@classmethod
	def load_vote(cls, user_uuid4, task_uuid4):
		# stub
		pass


	@classmethod
	def load_all_votes_by_task(cls, task_uuid4):
		# stub
		return ()


	@classmethod
	def update_vote(cls, user_uuid4, task_uuid4, vote_variant):
		# stub
		pass


	@classmethod
	def get_vote_api_formatted_data(cls, vote):
		return {
			'uuid4': vote.uuid4,
			'user_uuid4': vote.user_uuid4,
			'task_uuid4': vote.task_uuid4,
			'variant': vote.variant
		}

