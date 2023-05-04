import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    counter: 0
  },
  // store의 computed 역할
  // state의 값을 변경하지 않으면서 원하는 값을 반환하고 싶을 때
  getters: {
    getPlusCounter(state){
      console.log("getters 호출!")
      // 가능은하다!
      // state에 직접 접근은 절대 하지말자
      // state.counter += 10
      return state.counter
    }
  },
  mutations: {
    // 이름은 대문자로, 스네이크 케이스로 구현을 권장
    // mutation 의 파라미터: state, data
    // state: store 에 저장된 전체 데이터
    // data: commit 하는 쪽에서 전달해주는 데이터
    PLUS_COUNTER(state){
      state.counter++
    },
    MINUS_COUNTER(state){
      state.counter--
    }
  },
  actions: {
    plusCounter(context) {
      console.log('context: ', context)
      // 직접 접근도 가능하다
      // 하지만 이런식으로 하지는 말자
      // context.state.counter++
      context.commit("PLUS_COUNTER")
    },
    minusCounter(context) {
      console.log('context: ', context)
      context.commit("MINUS_COUNTER")
    }

  },
  modules: {
  }
})
