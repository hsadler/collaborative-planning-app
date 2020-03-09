import uuid

from data_store.mysql_driver import MySqlDriver
from data_struct.vote_variant import VoteVariant


class VoteVariantService():

	"""
	VoteVariant Service. Handles vote variant related business logic.
	"""

	VOTE_VARIANT_TABLE = 'vote_variant'	


	@classmethod
	def load_all_vote_variants(cls):
		sql = """
			SELECT * FROM {0}
		""".format(cls.VOTE_VARIANT_TABLE)
		success, query_result = MySqlDriver.query_bind(sql)
		vote_variants = [
			VoteVariant(
				vote_variant_record['uuid4'], 
				vote_variant_record['variant']
			) for
			vote_variant_record in query_result
		]
		return vote_variants


	@classmethod
	def get_vote_variant_api_formatted_data(cls, vote_variant):
		return {
			'uuid4': vote_variant.uuid4,
			'variant': vote_variant.variant
		}
