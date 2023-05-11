import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
const BASE_URL = 'http://localhost:8000/'
const TODO_LIST_URL = BASE_URL + 'todos/'

import axios from 'axios'
import router from '../router/index'

export default new Vuex.Store({
  state: {
    todos: [
      // {
      //   title: '제목1',
      //   description: '내용1',
      //   is_completed: false,
      // },
    ]
  },
  getters: {
  },
  mutations: {
    GET_TODOS(state, todos) {
      state.todos = todos
    }
  },
  actions: {
    // 재사용 가능성이 높으므로 action에 작성
    getTodos(context) {
      // console.log(context)
      axios({
        method: 'get',
        url: TODO_LIST_URL
      })
      .then((response) => {
        // console.log(response)
        context.commit("GET_TODOS", response.data)
      })
      .catch((error) => {
        console.log(error)
      })
    },
    deleteTodo(context, todo){
      axios({
        method: 'delete',
        url: TODO_LIST_URL+todo.id+'/'
      })
      .then((res) => {
        console.log(res, '테스트')
        router.push({name: 'todos'})
      })
      .catch((error) => {
        console.log(error)
      })

    }
  },
  modules: {
  }
})
