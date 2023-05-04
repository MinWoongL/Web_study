import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todos: [
      {
        title: '할일 1',
        isCompleted: false,
      },
      {
        title: '할일 2',
        isCompleted: false,
      },
    ]
  },
  getters: {
  },
  mutations: {
    // 실제로 직접 state를 변경해주는곳
    CREATE_TODO(state, todoItem) {
      state.todos.push(todoItem)
      console.log(state.todos)
    }
  },
  actions: {
    // context, payload
    createTodo(context, todoTitle) {
      // todotitle만 받아오고 isCompleted는 없으므로 직접 넣어줌
      const todoItem = {
        title: todoTitle,
        isCompleted: false,
      }
      // mutation으로 넘겨줌
      context.commit('CREATE_TODO', todoItem)
      
    }
  },
  modules: {
  }
})
