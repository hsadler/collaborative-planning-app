<template>
	<div class="user-create-container">
		<h1>Create User</h1>
		<form @submit.prevent="createUser">
			<input 
				type="text"
				v-model="userName" 
				placeholder="your name" 
				maxlength="100"
				autocomplete="off"
			/><button id="user-name-submit" type="submit">Submit</button>
			<br>
			<p 
				class="submission-error" 
				v-if="showSubmissionError"
			>{{submissionErrorMessage}}</p>
		</form>
	</div>
</template>

<script>
import services from '@/services'

export default {
	name: 'UserCreate',
	props: {},
	data () {
		return {
			httpService: services.use('httpService'),
			userService: services.use('userService'),
			userName: null,
			minCharacters: 2,
			showSubmissionError: false,
			submissionErrorMessage: ''
		}
	},
	methods: {
		createUser () {
			this.showSubmissionError = false
			if(this.userName.length < this.minCharacters) {
				this.showSubmissionError = true
				this.submissionErrorMessage = 'name must be at least ' + 
					this.minCharacters + ' characters'
				return
			}
			var data = {
				user_name: this.userName
			}
			this.httpService.post('/api/create-user', data).then((res) => {
				if(res.success) {
					this.userService.setUser(res.user)
					this.$router.push('/tasks')
				} else {
					var userName = this.userName
					this.showSubmissionError = true
					this.submissionErrorMessage = 'user name "' + userName + 
						'" already taken'
					this.userName = null
				}
			})
		}
	},
	created () {}
}
</script>

<style scoped lang="scss">
	div.user-create-container {
		button#user-name-submit {
			margin-left: 10px;
		}
		p.submission-error {
			font-size: 0.8em;
			color: red;
		}
	}
</style>
