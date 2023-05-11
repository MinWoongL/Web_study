<template>
  <div>
    <h1>RealDetail</h1>
    <div v-if="!todo">
      <p>로딩 중</p>
    </div>
    <div v-else>
      <h4> 글 번호 : {{ todo.id }} </h4>
      <p> 제목 : {{ todo.title }} </p>
      <p> 설명 : {{ todo.description }}</p>
      <p> 완료여부 : {{ todo.is_completed }} </p>
      <button @click="deleteTodo()">삭제</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const TODO_URL = 'http://localhost:8000'
export default {
    name: "TodoRealDetail",
    data() {
        return {
          todo: null,
        }
    },
    created(){
      this.getTodoDetail()
    },
    methods: {
      getTodoDetail(){
        // console.log(this.$route.params)
        axios({
          method: 'get',
          url: `${TODO_URL}/todos/${this.$route.params.id}/`
        })
        .then((response) => {
          // console.log(response)
          this.todo = response.data
        })
        .catch((error) => {
          console.log(error)
        })
      },
      deleteTodo() {
        this.$store.dispatch('deleteTodo', this.todo)
      }
    }
}
</script>

<style>

</style>