<template>
<div>
  <h2>Props Emit 을 공부하자!</h2>
  <IncomeComponent/>
</div>
</template>

<script>
import IncomeComponent from '../components/propsEmit/IncomeComponent.vue'
export default {
  name: 'PropsEmitView',
  components: {
    IncomeComponent
  },
}
</script>

<style>

</style>