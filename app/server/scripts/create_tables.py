
import sys
sys.path.append('..')

from data_store.mysql_driver import MySqlDriver
from utils.print import ppp


# create user table
create_user_table_query = """
	CREATE TABLE IF NOT EXISTS user (
		`uuid4` VARCHAR(32) PRIMARY KEY,
		`name` VARCHAR(255) NOT NULL UNIQUE
	)
"""
query_result = MySqlDriver.query_bind(query_string=create_user_table_query)
ppp('result of create "user" table query:', query_result)


# create task table
create_task_table_query = """
	CREATE TABLE IF NOT EXISTS task (
		`uuid4` VARCHAR(32) PRIMARY KEY,
		`title` VARCHAR(1000) NOT NULL
	)
"""
query_result = MySqlDriver.query_bind(query_string=create_task_table_query)
ppp('result of create "task" table query:', query_result)


# create vote table
create_vote_table_query = """
	CREATE TABLE IF NOT EXISTS vote (
		`uuid4` VARCHAR(32) PRIMARY KEY,
		`variant` VARCHAR(32) NOT NULL,
		`user_uuid4` VARCHAR(32) NOT NULL,
		`task_uuid4` VARCHAR(32) NOT NULL,
		UNIQUE KEY (`user_uuid4`, `task_uuid4`)
	)
"""
query_result = MySqlDriver.query_bind(query_string=create_vote_table_query)
ppp('result of create "vote" table query:', query_result)


# create vote_variant table
create_vote_variant_table_query = """
	CREATE TABLE IF NOT EXISTS vote_variant (
		`uuid4` VARCHAR(32) PRIMARY KEY,
		`variant` VARCHAR(32) NOT NULL UNIQUE
	)
"""
query_result = MySqlDriver.query_bind(query_string=create_vote_variant_table_query)
ppp('result of create "vote_variant" table query:', query_result)


