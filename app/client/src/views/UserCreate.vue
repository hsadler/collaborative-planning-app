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
				v-if="submissionError"
			>name must be at least {{minCharacters}} characters</p>
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
			submissionError: false
		}
	},
	methods: {
		createUser () {
			this.submissionError = false
			if(this.userName.length < this.minCharacters) {
				this.submissionError = true
				return
			}
			var url = '/api/create-user'
			var params = {
				user_name: this.userName
			}
			this.httpService.get(url, params).then((res) => {
				if(res.success) {
					this.userService.setUser(res.user)
					this.$router.push('/tasks')
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
