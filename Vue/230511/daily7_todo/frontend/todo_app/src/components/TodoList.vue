<template>
  <div>
    <h1>TodoList</h1>
    <hr>
    <div v-if="!todos">
      <p>로딩 중....</p>
    </div>
    <div v-else>
      <div v-for="todo in todos" :key="todo.id">
        <TodoDetail :todo ="todo"/>

        <!-- <h4> 글 번호 : {{ todo.id }} </h4>
        <p> 제목 : {{ todo.title }} </p>
        <p> 설명 : {{ todo.description }}</p>
        <router-link :to="{name: 'TodoDetail', params: {id: todo.id}}">
          - 상세정보 -
        </router-link> -->
      <hr>
    </div>

    </div>
    
  </div>
</template>

<script>
import TodoDetail from './TodoDetail.vue'

export default {
    name: "TodoList",
    components: {
      TodoDetail
    },
    data() {
        return {

        }
    },
    computed: {
      todos() {
        return this.$store.state.todos.length === 0 ?
        false : this.$store.state.todos
      }

    },
    created() {
      this.$store.dispatch('getTodos')
    }

}
</script>

<style>

</style>