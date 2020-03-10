<template>
	<div class="user-select-container">
		<h1>Select User</h1>
	</div>
</template>

<script>
import services from '@/services'

export default {
	name: 'UserSelect',
	props: {},
	data () {
		return {
			httpService: services.use('httpService')
		}
	},
	methods: {
		selectUser (userName) {
			return userName
			// TODO
		}
	},
	created () {
		// TODO: FETCH USERS
	}
}
</script>

<style scoped lang="scss">
	div.user-select-container {}
</style>
