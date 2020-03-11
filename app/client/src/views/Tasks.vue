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
			socketService: services.use('socketService'),
			socket: null,
			newTaskTitle: null,
			tasks: [],
			minCharacters: 2,
			submissionError: false
		}
	},
	methods: {
		createTask () {
			this.submissionError = false
			if(
				!this.newTaskTitle || 
				this.newTaskTitle.length < this.minCharacters
			) {
				this.submissionError = true
				return
			}
			var params = {
				task_title: this.newTaskTitle
			}
			this.socket.emit('create_task', params)
			this.newTaskTitle = null
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
		// create socket and listeners
		this.socket = this.socketService.io()
		this.socket.on('task_created', (task) => {
			this.tasks.push(task)
		});
		// fetch all tasks
		var url = '/api/get-all-tasks'
		this.httpService.get(url).then((res) => {
			if(res.success) {
				this.tasks = this.tasks.concat(res.tasks)
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
