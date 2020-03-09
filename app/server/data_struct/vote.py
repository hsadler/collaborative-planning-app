

class Vote():
	"""
	Vote Struct
	"""

	def __init__(self, uuid4, user_uuid4, task_uuid4, variant):
		self.uuid4 = uuid4
		self.user_uuid4 = user_uuid4
		self.task_uuid4 = task_uuid4
		self.variant = variant
