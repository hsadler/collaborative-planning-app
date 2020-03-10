<template>
	<div class="user-select-container">
		<h1>Select User</h1>
		<ul>
			<li
				v-for="(user, index) in users" 
				:key="index"
				@click="selectUser(user)"
			>{{ user.name }}</li>
		</ul>
	</div>
</template>

<script>
import services from '@/services'

export default {
	name: 'UserSelect',
	props: {},
	data () {
		return {
			httpService: services.use('httpService'),
			userService: services.use('userService'),
			users: []
		}
	},
	methods: {
		selectUser (user) {
			this.userService.setUser(user)
			this.$router.push('/tasks')
		}
	},
	created () {
		var url = '/api/get-all-users'
		this.httpService.get(url).then((res) => {
			if(res.success) {
				this.users = res.users
			}
		})
	}
}
</script>

<style scoped lang="scss">
	div.user-select-container {
		ul {
			li {
				color: #42b983;
				cursor: pointer;
			}
		}
	}
</style>
