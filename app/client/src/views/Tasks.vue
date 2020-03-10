<template>
	<div class="tasks-container">
		<h1>Tasks</h1>
	</div>
</template>

<script>
import services from '@/services'

export default {
	name: 'Tasks',
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
	created () {
		// TODO: fetch all tasks
	}
}
</script>

<style scoped lang="scss">
	div.tasks-container {}
</style>
