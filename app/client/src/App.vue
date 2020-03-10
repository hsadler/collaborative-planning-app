<template>
	<div id="app">
		<Navigation></Navigation>
		<router-view/>
	</div>
</template>

<script>
import Navigation from '@/components/Navigation'

export default {
	name: 'App',
	components: {
		Navigation
	}
}
</script>

<style lang="scss">
	#app {
		font-family: Avenir, Helvetica, Arial, sans-serif;
		-webkit-font-smoothing: antialiased;
		-moz-osx-font-smoothing: grayscale;
		padding: 30px;
		color: #2c3e50;
		h1 {
			font-size: 3em;
		}
		a {
			color: #2c3e50;
			&:visited {
				color: #2c3e50;
			}
			&.router-link-exact-active {
				color: #42b983;
			}
		}
	}
</style>
