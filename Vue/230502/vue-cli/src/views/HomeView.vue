<template>
<!-- template 태그 아래에는 하나의 태그만 있어야한다. -->
<div>
  <h1>Home View</h1>
  <TodoList/>
</div>
</template>

<script>
import TodoList from '../components/TodoList.vue'

export default {
    name: 'HomeView',
    components: {
        TodoList,
    }

    
}
</script>

// scoped: 현재 컴포넌트에만 적용
// 자식에게도 적용이 안됨
<style scoped>
h1 {
    color: blue;
}
/* >>> : 딥 셀렉터 - 부모 컴포넌트에서 자식 컴포넌트의 CSS로 접근 */
/* /deep/ .h1-child, ::v-deep(.h1-child) 처럼 적어도 가능함 */

/* /deep/ .h1-child {
    color: gold
} */

/* ::v-deep(.h1-child){
    color: yellowgreen
} */
div >>> .h1-child {
    color: green
}
</style>




// global
<style>
h1 {
    color: violet;
}
</style>