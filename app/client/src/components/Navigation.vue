<template>
	<div class="navigation-container">
		<router-link id="home" to="/">Home</router-link>
		<router-link v-if="true" id="tasks" to="/tasks">Tasks</router-link>
	</div>
</template>

<script>
export default {
	name: 'Navigation',
	props: {}
}
</script>

<style scoped lang="scss">
	div.navigation-container {
		padding: 30px 0;
		a {
			font-weight: bold;
			&#tasks {
				float: right
			}
		}
	}
</style>
