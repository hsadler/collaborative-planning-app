

class Task():
	"""
	Task Struct
	"""

	def __init__(self, uuid4, variant, user_uuid4, task_uuid4):
		self.uuid4 = uuid4
		self.variant = variant
		self.user_uuid4 = user_uuid4
		self.task_uuid4 = task_uuid4
