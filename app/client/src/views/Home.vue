<template>
	<div class="home-container">
		<h1>Collaborative Planning App</h1>
		<router-link to="/user-create">create user</router-link>
		<router-link class="margin-left" to="/user-select">select user</router-link>
	</div>
</template>

<script>
export default {
	name: 'HomePage',
	props: {},
	data () {
		return {}
	},
	methods: {}
}
</script>

<style scoped lang="scss">
	div.home-container {
		a.margin-left {
			margin-left: 30px;
		}
	}
</style>
