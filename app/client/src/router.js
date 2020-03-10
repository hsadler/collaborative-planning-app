import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/Home'
import Task from '@/views/Task'
import ChatRoom from '@/views/ChatRoom'
import NotFound from '@/views/NotFound'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/task',
      name: 'Task',
      component: Task
    },
    {
      path: '/chat-room',
      name: 'ChatRoom',
      component: ChatRoom
    },
    // {
    //   path: '/edit-message/:uuid',
    //   name: 'EditWallMessage',
    //   component: EditWallMessage
    // },
    {
      path: '*',
      name: 'NotFound',
      component: NotFound
    }
  ]
})
