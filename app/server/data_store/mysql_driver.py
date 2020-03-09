import MySQLdb as mdb
import config.config as config


class MySqlDriver():


	@classmethod
	def query_bind(self, query_string, bind_vars={}):
		"""
		Performs a MySQL query from a raw query string and returns the result.
		Uses bound variables to protect against SQL injection.

		Args:
			query_string (str): formatted MySQL query string.
				Ex. 'SELECT * FROM table where id=:id'
			bind_vars (dict): named variables to be escaped and injected into
				the query string.
				Ex. { 'id': 1234 }

		Returns:
			(tuple) Tuple of dictionary representations of records.

		"""

		for key, val in bind_vars.items():
			bind_str = ':{0}'.format(key)
			if bind_str in query_string:
				query_string = query_string.replace(
					bind_str,
					'%({0})s'.format(key)
				)
		conn, cur = self.connect()
		cur.execute(query_string, bind_vars)
		conn.close()
		return cur.fetchall()


	@classmethod
	def connect(self):
		conn = mdb.connect(
			host=config.MYSQL_HOST,
			user=config.MYSQL_USER,
			passwd=config.MYSQL_PASSWORD,
			db=config.MYSQL_DB_NAME
		)
		cur = conn.cursor(mdb.cursors.DictCursor)
		conn.set_character_set('utf8')
		cur.execute('SET NAMES utf8;')
		cur.execute('SET CHARACTER SET utf8;')
		cur.execute('SET character_set_connection=utf8;')
		return conn, cur

