import uuid
import sys
sys.path.append('..')

from data_store.mysql_driver import MySqlDriver
from utils.print import ppp


# populate vote_variant table
variants = ['0', '1/2', '1', '2', '3', '5', '8', '13']
for variant in variants:
	uuid4 = uuid.uuid4().hex
	populate_sql = """
		INSERT INTO vote_variant (uuid4, variant)
		VALUES (:uuid4, :variant)
	"""
	bind_vars = {
		'uuid4': uuid4,
		'variant': variant
	}
	query_result = MySqlDriver.query_bind(populate_sql, bind_vars)
	ppp('result of populate vote_variant table query:', query_result)
	