<template>
	<div class="task-container">

		<h1>Task: <span class="task-title">{{getTaskTitle}}</span></h1>

		<!-- TODO: votes will go here -->

	</div>
</template>

<script>
import services from '@/services'

export default {
	name: 'Task',
	props: {
		taskId: String
	},
	data () {
		return {
			httpService: services.use('httpService'),
			socketService: services.use('socketService'),
			task: null
		}
	},
	methods: {},
	computed: {
		getTaskTitle() {
			if(this.task) {
				return this.task.title
			}
			return ''
		}
	},
	created () {
		// fetch task
		var url = '/api/get-task-by-id'
		var params = {
			task_id: this.taskId
		}
		this.httpService.get(url, params).then((res) => {
			if(res.success) {
				this.task = res.task
			}
		})
	}
}
</script>

<style scoped lang="scss">
	div.task-container {
		h1 {
			span.task-title {
				color: #42b983;	
			}
		}
	}
</style>
