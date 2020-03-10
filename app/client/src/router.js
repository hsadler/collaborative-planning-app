import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/Home'
import UserCreate from '@/views/UserCreate'
import UserSelect from '@/views/UserSelect'
import Tasks from '@/views/Tasks'
import Task from '@/views/Task'
import ChatRoom from '@/views/ChatRoom'
import NotFound from '@/views/NotFound'

Vue.use(Router)

export default new Router({
  // BUG: enabling this causes a refresh issue for dynamic routes
  // mode: 'history', 
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/user-create/',
      name: 'UserCreate',
      component: UserCreate
    },
    {
      path: '/user-select/',
      name: 'UserSelect',
      component: UserSelect
    },
    {
      path: '/tasks/',
      name: 'Tasks',
      component: Tasks
    },
    {
      path: '/task/:taskId/',
      name: 'Task',
      component: Task,
      props: true
    },
    // test route
    {
      path: '/chat-room/',
      name: 'ChatRoom',
      component: ChatRoom
    },
    {
      path: '*',
      name: 'NotFound',
      component: NotFound
    }
  ]
})
