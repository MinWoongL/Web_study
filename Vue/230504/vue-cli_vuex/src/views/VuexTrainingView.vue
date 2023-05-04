<template>
  <div>
    <h2>Vuex 공부하기</h2>
    <!-- store 에 저장된 counter 출력 -->
    <!-- $ = 전역적으로 사용된다. -->
    <p>카운터: {{ counter }}</p>
    <p><button @click="count_up()">+</button><button @click="count_down()">-</button></p>
    <hr>
    {{ getCounter }}
  </div>
</template>

<script>
export default {
    name: "VuexTraningView",
    computed: {
        counter() {
            return this.$store.state.counter
        },
        getCounter() {
            console.log('computed 호출')
            return this.$store.getters.getPlusCounter
        }
    },
    methods: {
        count_up() {
            this.$store.dispatch('plusCounter')
            // 직접 접근으로도 수정가능
            // this.$store.state.counter += 1
        },
        count_down() {
            this.$store.dispatch('minusCounter')
            // this.$store.state.counter -= 1
        }
    },

}
</script>

<style>

</style>