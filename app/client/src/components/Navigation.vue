<template>
	<div class="navigation-container">
		<router-link to="/">Home</router-link> 
		&nbsp;|&nbsp;
		<router-link to="/tasks">Tasks</router-link>
		<span class="user" v-if="showUser()">User: {{userName}}</span>
	</div>
</template>

<script>
import services from '@/services'

export default {
	name: 'Navigation',
	props: {},
	data () {
		return {
			userService: services.use('userService')
		}
	},
	methods: {
		showUser() {
			return !!this.userService.getUser()
		}
	},
	computed: {
		userName() {
			return this.userService.getUser().name
		}
	}
}
</script>

<style scoped lang="scss">
	div.navigation-container {
		padding-top: 30px;
		a {
			font-weight: bold;
		}
		span.user {
			float: right
		}
	}
</style>
