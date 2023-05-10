import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import HelloView from '@/views/HelloView.vue'
import LoginView from '@/views/LoginView.vue'
import NotFound404 from '@/views/NotFound404.vue'
import DogView from '../views/DogView.vue'

Vue.use(VueRouter)

const isLoggedIn = true

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
    path: '/hello/:userName',
    name: 'hello',
    component: HelloView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
    // 라우터 가드
    beforeEnter(to, from, next) {
      if (isLoggedIn === true) {
        console.log('이미 로그인함')
        next({ name: 'home' })
      } else {
        next()
      }

    }
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '/dog/:breed',
    name: 'dog',
    component: DogView
  },
  // 요청한 리소스가 존재하지 않을 때,
  // 기존에 명시한 경로가 아닌 모든경로가 404 page로 redirect 됨
  // routes 최하단부에 작성
  {
    path: '*',
    redirect: '/404'
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// router/index.js
// router.beforeEach((to, from, next) => {
  // CODE HERE
  // console.log('to', to)
  // console.log('from', from)
  // console.log('next', next)
  // next()

  // 로그인 여부
  // const isLoggedIn = true  // 로그인 됨
  // const isLoggedIn = false  // 로그인 안됨

  // 로그인이 필요한 페이지
  // const authPages = ['hello', 'about', 'home']

  // allow페이지만두고 나머지를 모두 로그인이 필요한 페이지로 해도 된다.
  // const allowAuthPages = ['login']

  // 앞으로 이동할 페이지(to)가
  // 로그인이 필요한 사이트인지 확인
  // const isAuthRequired = authPages.includes(to.name)
  // const isAuthRequired = !allowAuthPages.includes(to.name)

  // if (isAuthRequired && !isLoggedIn) {
  //   console.log('Login으로 이동')
  //   next({ name: 'login' })
  // } else {
  //   console.log('to로 이동!')
  //   next()
  // }
// })
export default router
