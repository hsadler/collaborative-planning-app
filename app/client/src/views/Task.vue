<template>
	<div class="task-container">

		<h1>Task: <span class="task-title">{{getTaskTitle}}</span></h1>

		<table class="vote-variants">
			<tr>
				<th>Complexity</th>
				<th>Votes</th>
			</tr>
			<tr 
				class="data-row" 
				:class="{'user-voted': data.userVoted}"
				v-for="(data, variant) in getVariantToData" 
				:key="variant"
				@click="submitVote(variant)"
			>
				<td>{{variant}}</td>
				<td>{{data.voteCount}}</td>
			</tr>
		</table>
		
		<div class="select-user-link">
			<router-link v-if="userNotSelected" to="/user-select">
				select user in order to vote!
			</router-link>
		</div>

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
			userService: services.use('userService'),
			httpService: services.use('httpService'),
			socketService: services.use('socketService'),
			socket: null,
			task: null,
			voteVariants: [],
			votes: []
		}
	},
	methods: {
		submitVote(variant) {
			var user = this.userService.getUser()
			if(user) {
				var params = {
					user_id: user.uuid4,
					task_id: this.task.uuid4,
					vote_variant: variant
				}
				this.socket.emit('create_or_update_vote', params)
			}
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
				var user = this.userService.getUser()
				result[vote.variant]['votes'].push(vote)
				result[vote.variant]['voteCount'] += 1
				if(user && vote.user_uuid4 === user.uuid4) {
					result[vote.variant]['userVoted'] = true
				}
			})
			return result
		},
		userNotSelected() {
			return this.userService.getUser() === null
		}
	},
	created () {
		// create socket and listeners
		this.socket = this.socketService.io()
		this.socket.on('refresh_votes', (votes) => {
			this.votes = votes
		})
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
			td, th {
				text-align: left;
				padding: 10px;
			}
			td {
				cursor: pointer;
			}
			tr {
				&.data-row {
					&.user-voted {
						background-color: #86d4b1 !important;
					}
					&:hover {
						background-color: #bcebd6;
					}
				}
				&:nth-child(even) {
					background-color: #f3f3f3;
				}
			}
		}
		div.select-user-link {
			margin-top: 20px;
		}
	}
</style>
