import Vue from 'vue'
import VueRouter from 'vue-router'
import TheLunch from '../views/TheLunch'
import TheLotto from '../views/TheLotto.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/lunch',
    name: 'Lunch',
    component: TheLunch
  },
  {
    path: '/lotto/6',
    name: 'Lotto',
    // 지연로딩
    // 한번에 받아오는게 아닌
    // 필요할 때 마다 서버로 요청
    // 초기 로딩이 빠름
    // 서버로 추가적인 요청 발생
    component: () => import(/* webpackChunkName: "about" */ '../views/TheLotto.vue')
  },
  {
    path: '/lotto/:count',
    name: 'lotto',
    component: TheLotto
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
