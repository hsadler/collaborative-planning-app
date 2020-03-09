
import sys
sys.path.append('..')

import config.config as config
from data_store.mysql_driver import MySqlDriver
from utils.print import ppp


# create user table
create_user_table_query = """
	CREATE TABLE IF NOT EXISTS user (
		`uuid4` VARCHAR(32) PRIMARY KEY,
		`name` VARCHAR(255) NOT NULL
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
		`variant` tinyint(3) UNSIGNED NOT NULL,
		`user_uuid4` VARCHAR(32) NOT NULL,
		`task_uuid4` VARCHAR(32) NOT NULL
	)
"""
query_result = MySqlDriver.query_bind(query_string=create_vote_table_query)
ppp('result of create "vote" table query:', query_result)

