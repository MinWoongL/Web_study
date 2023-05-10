import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import ProfileView from '../views/ProfileView.vue'
import store from '../store/index'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
    // 해당 라우터에서만 특수하게 쓰는 경우
    // 로그인뷰는 로그인한 사용자는 못들어오도록 설정
    beforeEnter(to, from, next) {
      if(store.getters.isLoggedIn){
        alert('이미 로그인 됨')
        next({ name: 'home' })
      }
      next()
    }
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView,
  },


]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// 공통적으로 많이 쓰이는 Guard
router.beforeEach((to, from, next) => {
  const isLoggedIn = store.getters.isLoggedIn
  // 로그인이 필요한 페이지 목록
  const loginRequired = ['profile']
  if(loginRequired.includes(to.name) && !isLoggedIn) {
    alert('로그인이 필요합니다.')
    next({ name: 'login' })
  }
  next()
})

export default router
