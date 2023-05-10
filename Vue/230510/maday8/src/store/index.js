import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    users: [
      {
        id: 'admin',
        pw: '1234',
        idAdmin: true,
      },
      {
        id: 'test',
        pw: '123456',
        idAdmin: false,
      },

    ],
    // 비어있으면 로그인 x, 성공적으로 로그인하면 객체를 넣어줌.
    loginUser: {}
  },
  getters: {
    isLoggedIn(state) {
      // state의 loginUser 가 비어있다면 false /아니라면 true 반환
      // if(Object.keys(state.loginUser).length === 0){
      //   return false
      // } else {
      //   return true
      // }

      // 삼항연산자
      return Object.keys(state.loginUser).length !== 0 ? true: false

    },
  },
  mutations: {
    LOGIN(state, user) {
      state.loginUser = user
    }
  },
  actions: {
    login(context, form) {
      // state.user 에 form.id 와 같은 유저가 있는가?
      // 없다면 -> 그런 사용자는 없다!
      const user = context.state.users.find((user) => {
        return user.id === form.id
      })
      // 없었다면 undefined 반환
      if (!user) {
        // alert('해당 사용자는 없습니다')
        return Promise.reject('존재하지 않는 사용자입니다')
      }
      // 해당 유저의 pw 가 form.pw와 같은가?

      if (user.pw !== form.pw) {
        // alert('비밀번호가 다릅니다')
        return Promise.reject('PW가 다릅니다')
      }

      context.commit("LOGIN", user)

    }
  },
  modules: {
  }
})
