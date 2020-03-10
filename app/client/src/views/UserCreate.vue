<template>
	<div class="user-create-container">
		<h1>Create User</h1>
	</div>
</template>

<script>
import services from '@/services'

export default {
	name: 'UserCreate',
	props: {},
	data () {
		return {
			httpService: services.use('httpService')
		}
	},
	methods: {
		createUser (userName) {
			// TODO
		}
	},
	created () {}
}
</script>

<style scoped lang="scss">
	div.user-create-container {}
</style>
