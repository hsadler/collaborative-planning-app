import uuid

from data_store.mysql_driver import MySqlDriver
from data_struct.user import User


class UserService():

	"""
	User Service. Handles user related business logic.
	"""
	
	USER_TABLE = 'user'	


	@classmethod
	def create_user(cls, user_name):
		user_uuid4 = uuid.uuid4().hex
		user = User(user_uuid4, user_name)
		# save to db
		sql = """
			INSERT INTO {0} (uuid4, name) 
			VALUES (:uuid4, :name)
		""".format(cls.USER_TABLE)
		bind_vars = {
			'uuid4': user.uuid4,
			'name': user.name
		}
		success, query_result = MySqlDriver.query_bind(sql, bind_vars)
		return user if success else None


	@classmethod
	def load_all_users(cls):
		sql = """
			SELECT * FROM {0}
		""".format(cls.USER_TABLE)
		success, query_result = MySqlDriver.query_bind(sql)
		if success and query_result is not None:
			users = [
				User(user_record['uuid4'], user_record['name']) for
				user_record in query_result
			]
			return users
		return None

	
	@classmethod
	def get_user_api_formatted_data(cls, user):
		return {
			'uuid4': user.uuid4,
			'name': user.name
		}

