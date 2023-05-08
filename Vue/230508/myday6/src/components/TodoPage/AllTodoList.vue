<template>
  <div>
    <h3>모든 할 일</h3>
    <!-- {{ todoList }} -->
    <div v-for="(item, index) in todoList" :key="item.id">
      {{index + 1}} -  {{ item.content }}
      <button @click="deleteTodo(item)">Delete</button>
    </div>

    <h3>Todo</h3>
    <input type="text" v-model.trim='todoTitle' @keyup.enter="createTodo">
    <br>
    <button @click="loadTodos">데이터 불러오기</button>
    {{ todoTitle }}

  </div>
</template>

<script>
// import { mapState } from 'vuex'
export default {
    name: "AllTodoList",
    computed: {
        todoList() {
            // 순서 헷갈리지 말기
            // todo 모듈의 state 접근
            // state.todo.todoList
            return this.$store.state.todo.todoList
        },

    },
    data() {
        return {
            todoTitle: ''
        }
    },
    // 만들어질때 loadtodoList를 호출해서 LocalStorage 데이터까지 모두 출력
    created() {
        this.$store.dispatch('loadTodoList')
    },
    methods: {
        createTodo() {
            // 비어있지 않다면, store에 저장
            if(this.todoTitle){
                console.log(this.todoTitle)
                this.$store.dispatch('createTodo', this.todoTitle)
            } else {
                alert('내용을 입력하세요')
            }
        },
        deleteTodo(todo) {
            console.log(todo)
            this.$store.dispatch('deleteTodo', todo)
        },
        loadTodos() {
            this.$store.dispatch('loadTodoList')
        },
        
    }

}
</script>

<style>

</style>