
import Vue from 'vue'
import App from '@/App'
import router from '@/router'
import services from '@/services'
import httpService from '@/services/httpService'
import socketService from '@/services/socketService'
import userService from '@/services/userService'


Vue.config.productionTip = false

services.registerServices({
  httpService,
  socketService,
  userService
})

new Vue({
	router,
	mounted() {
		var lsUser = localStorage.getItem('user')
		if (lsUser) {
			var user = JSON.parse(lsUser)
			userService.setUser(user);
		}
	},
	render: h => h(App),
}).$mount('#app')
