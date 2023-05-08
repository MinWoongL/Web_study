import Vue from 'vue'
import VueRouter from 'vue-router'
import AllTodoList from '../components/TodoPage/AllTodoList.vue'
import ImportantTodoList from '../components/TodoPage/ImportantTodoList.vue'
import TodayTodoList from '../components/TodoPage/TodayTodoList.vue'

Vue.use(VueRouter)

const routes = [
  // {
  //   path: '/',
  //   name: 'home',
  //   component: HomeView
  // },
  {
    path: '/All',
    name: 'AllTodoList',
    component: AllTodoList
  },
  {
    path: '/Important',
    name: 'ImportantTodoList',
    component: ImportantTodoList
  },
  {
    path: '/Today',
    name: 'TodayTodoList',
    component: TodayTodoList
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
