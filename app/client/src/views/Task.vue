<template>
	<div class="task-container">

		<h1>Task: <span class="task-title">{{getTaskTitle}}</span></h1>

		<table class="vote-variants">
			<tr>
				<th>Complexity</th>
				<th>Votes</th>
			</tr>
			<tr 
				v-for="(data, variant) in getVariantToData" 
				:key="variant"
				@click="submitVote(variant)"
			>
				<td>{{variant}}</td>
				<td>{{data.voteCount}}</td>
			</tr>
		</table>

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
			userService: services.use('userService'),
			task: null,
			voteVariants: [],
			votes: []
		}
	},
	methods: {
		submitVote(variant) {
			var params = {
				user_id: this.userService.getUser().uuid4,
				task_id: this.task.uuid4,
				vote_variant: variant
			}
			this.httpService.get(
				'/api/create-or-update-vote', 
				params
			).then((res) => {
				if(res.success) {
					console.log('vote cast:')
					console.log(res.vote)
				}
			})
		},
		getVotesFromVariant(variant) {
			if(variant.voteValue) {
				return variant.voteValue
			} else {
				return ''
			}
		}
	},
	computed: {
		getTaskTitle() {
			if(this.task) {
				return this.task.title
			}
			return ''
		},
		getVariantToData() {
			var result = {}
			this.voteVariants.forEach((voteVariant) => {
				result[voteVariant.variant] = {
					'voteVariant': voteVariant,
					'votes': [],
					'voteCount': 0
				}
			})
			this.votes.forEach((vote) => {
				result[vote.variant]['votes'].push(vote)
				result[vote.variant]['voteCount'] += 1
			})
			return result
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
				this.voteVariants = res.vote_variants
				// fetch votes
				params = { task_id: this.taskId }
				this.httpService.get(
					'/api/get-all-votes-by-task', 
					params
				).then((res) => {
					if(res.success) {
						this.votes = res.votes
					}
				})		
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
		table {
			border-collapse: collapse;
			width: 100%;
		}
		td, th {
			border: 1px solid #dddddd;
			text-align: left;
			padding: 8px;
		}
		td {
			cursor: pointer;
		}
		tr:nth-child(even) {
			background-color: #dddddd;
		}
	}
</style>
