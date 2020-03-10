<template>
	<div class="task-container">

		<h1>Task</h1>

	</div>
</template>

<script>
import services from '@/services'

export default {
	name: 'Task',
	props: {},
	data () {
		return {
			httpService: services.use('httpService'),
			socketService: services.use('socketService')
		}
	},
	methods: {},
	created () {
		// TESTING
		var url = '/api/get-all-users'
		this.httpService.get(url).then((res) => {
			console.log(res)
		})
		var socket = this.socketService.io()
		console.log(socket)
	}
}
</script>

<style scoped lang="scss">
	div.task-container-container {}
</style>
