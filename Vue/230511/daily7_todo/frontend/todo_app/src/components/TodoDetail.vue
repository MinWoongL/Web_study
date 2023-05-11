<template>
  <div>
    <div>
        <h4> 글 번호 : {{ todo.id }} </h4>
        <p> 제목 : {{ todo.title }} </p>
        <p> 설명 : {{ todo.description }}</p>
        <router-link :to="{name: 'todo-detail', params: {id: todo.id}}">
          - 상세정보 -
        </router-link>
    </div>
  </div>
</template>

<script>


export default {
    name: "TodoDetail",
    components: {
        
    },
    data() {
        return {

        }
    },
    props: {
        todo: Object,
    }

}
</script>

<style>

</style>