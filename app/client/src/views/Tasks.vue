<template>
	<div class="tasks-container">
		
		<h1>Tasks</h1>

		<!-- create task form -->
		<form @submit.prevent="createTask">
			<input 
				type="text"
				v-model="newTaskTitle" 
				placeholder="task title" 
				maxlength="100"
				autocomplete="off"
			/><button id="task-title-submit" type="submit">Create New</button>
			<br>
			<p 
				class="submission-error" 
				v-if="submissionError"
			>task title must be at least {{minCharacters}} characters</p>
		</form>

		<!-- existing tasks list -->
		<ul>
			<li
				v-for="(task, index) in tasks" 
				:key="index"
				@click="selectTask(task)"
			>{{ task.title }}</li>
		</ul>

	</div>
</template>

<script>
import services from '@/services'

export default {
	name: 'Tasks',
	props: {},
	data () {
		return {
			httpService: services.use('httpService'),
			newTaskTitle: null,
			tasks: [],
			minCharacters: 2,
			submissionError: false
		}
	},
	methods: {
		createTask () {
			this.submissionError = false
			if(this.newTaskTitle.length < this.minCharacters) {
				this.submissionError = true
				return
			}
			// TODO: convert this to socket call
			var url = '/api/create-task'
			var params = {
				task_title: this.newTaskTitle
			}
			this.httpService.get(url, params).then((res) => {
				if(res.success) {
					this.newTaskTitle = null
					this.tasks.push(res.task)
				}
			})
		},
		selectTask (task) {
			this.$router.push({
				name: 'Task',
				params: {
					taskId: task.uuid4
				}
			})
		}
	},
	created () {
		var url = '/api/get-all-tasks'
		this.httpService.get(url).then((res) => {
			if(res.success) {
				this.tasks = res.tasks
			}
		})
	}
}
</script>

<style scoped lang="scss">
	div.tasks-container {
		button#task-title-submit {
			margin-left: 10px;
		}
		p.submission-error {
			font-size: 0.8em;
			color: red;
		}
		ul {
			li {
				color: #42b983;
				cursor: pointer;
			}
		}
	}
</style>
