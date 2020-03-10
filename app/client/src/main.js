
import Vue from 'vue'
import App from '@/App'
import router from '@/router'
import services from '@/services'
import httpService from '@/services/httpService'
import socketService from '@/services/socketService'


Vue.config.productionTip = false

services.registerServices({
  httpService,
  socketService
})

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
