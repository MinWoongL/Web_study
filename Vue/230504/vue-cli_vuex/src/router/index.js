import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import PropsEmitView from '../views/PropsEmitView.vue'
import WatchView from '../views/WatchView.vue'
import VuexTraining from '../views/VuexTrainingView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    // URI 경로
    path: '/props-emit',
    // 경로에 해당하는 이름
    name: 'props-emit',
    // 해당 경로 요청 시 보여줘야 할 컴포넌트 등록
    component: PropsEmitView
  },
  {
    path: '/watch-view',
    name: 'watch-view',
    component: WatchView
  },
  {
    path: '/vuex',
    name: 'vuex',
    component: VuexTraining
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
