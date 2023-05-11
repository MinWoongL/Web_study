<template>
  <div>
    <h1>할 일 생성</h1>
    <div>
      <label for="title-input">할일: </label>
      <input type="text" v-model="form.title">
    </div>
    <div>
      <label for="decription-input">설명: </label>
      <input type="text" v-model="form.description">
    </div>
    <br>
    <button @click="createTodo()">생성</button>
    <br>
    {{ form.title }}
    <br>
    {{ form.description }}

  </div>
</template>

<script>
import axios from 'axios'
const TODO_URL = 'http://localhost:8000'
export default {
    name: "CreateView",
    data() {
      return {
        form: {
          title: null,
          description: null
        }
      }
    },
    methods: {
      createTodo() {
        const title = this.form.title
        const description = this.form.description

        if(this.form.title === ''){
          alert('할 일을 입력해주세요')
          return
        }
        if(this.form.description === ''){
          alert('설명을 입력해주세요')
          return
        }

        axios({
          method: 'post',
          url: `${TODO_URL}/todos/`,
          data: {
            title,
            description
          }
        })
        .then(() => {
          this.$router.push({name: 'todos'})
          // console.log(response)
        })
        .catch((error) => {
          console.log(error)
        })

      }
      
    }
}
</script>

<style>

</style>