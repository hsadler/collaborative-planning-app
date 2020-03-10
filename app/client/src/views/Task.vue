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
			task: null,
			voteVariants: [],
			votes: []
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
		var params = {
			task_id: this.taskId
		}
		this.httpService.get('/api/get-task-by-id', params).then((res) => {
			if(res.success) {
				this.task = res.task
			}
		})
		// fetch vote variants
		this.httpService.get('/api/get-available-vote-variants').then((res) => {
			if(res.success) {
				console.log(res.vote_variants)
				this.voteVariants = res.vote_variants
			}
		})
		// fetch votes
		params = {
			task_id: this.taskId
		}
		this.httpService.get(
			'/api/get-all-votes-by-task', 
			params
		).then((res) => {
			if(res.success) {
				console.log(res.votes)
				this.votes = res.votes
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
