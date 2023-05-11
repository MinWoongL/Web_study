<template>
  <div>
    <h1>할 일 목록</h1>
    <button @click="getTodo()">Get Todos</button>
    <TodoList/>
    
  </div>
</template>

<script>
import TodoList from '../components/TodoList.vue'
import axios from 'axios'

export default {
  name: "TodoView",
  components: {
    TodoList
  },
  created() {
    const BACKEND_URL = 'http://localhost:8000/todos/test'
    axios.get(BACKEND_URL)
    .then((response) => {
      console.log(response)
    })
    .catch((error) => {
      console.log(error)
    })
  },
  methods: {
    getTodo() {
      this.$store.dispatch('getTodos')
    }
  }

}
</script>
