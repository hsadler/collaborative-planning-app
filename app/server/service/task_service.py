import uuid

from data_store.mysql_driver import MySqlDriver
from data_struct.task import Task


class TaskService():

	"""
	Task Service. Handles task related business logic.
	"""

	TASK_TABLE = 'task'	


	@classmethod
	def create_task(cls, task_title):
		task_uuid4 = uuid.uuid4().hex
		task = Task(task_uuid4, task_title)
		# save to db
		sql = """
			INSERT INTO {0} (uuid4, title) 
			VALUES (:uuid4, :title)
		""".format(cls.TASK_TABLE)
		bind_vars = {
			'uuid4': task.uuid4,
			'title': task.title
		}
		success, query_result = MySqlDriver.query_bind(sql, bind_vars)
		if not success:
			return None
		return task


	@classmethod
	def load_all_tasks(cls):
		sql = """
			SELECT * FROM {0}
		""".format(cls.TASK_TABLE)
		success, query_result = MySqlDriver.query_bind(sql)
		tasks = [
			Task(task_record['uuid4'], task_record['title']) for
			task_record in query_result
		]
		return tasks


	@classmethod
	def get_task_api_formatted_data(cls, task):
		return {
			'uuid4': task.uuid4,
			'title': task.title
		}
