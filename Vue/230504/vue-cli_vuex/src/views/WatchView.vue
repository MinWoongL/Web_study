<template>
  <div>
    <h2>Watch View!</h2>
    <p> 카운터: {{ counter }} </p>
    <p><button @click="count_up()">+</button><button @click="count_down()">-</button></p>
    <p> 베스트: {{ max_count }}</p>
    <p> 워스트: {{ min_count }}</p>
  </div>
</template>

<script>
export default {
    name: "WatchView",
    data() {
        return {
            counter: 0,
            max_count: 0,
            min_count: 0,
        }
    },
    methods: {
        count_up() {
            this.counter += 1
        },
        count_down() {
            this.counter -= 1
        }
    },
    watch: {
        // 변수가 변경될 때마다 자동으로 함수가 호출.
        counter(newValue, oldValue) {
            console.log(`${oldValue} -> ${newValue}`)
            if (this.counter > this.max_count){
                this.max_count = this.counter
            }
            if (this.counter < this.min_count){
                this.min_count = this.counter
            }
        }
    }
    // computed: {
    //     max_C() {
    //         if (this.counter > this.max_count) {
    //             return this.counter
    //         } else {
    //             return this.max_count
    //         }
    //     },
    //     min_C() {
    //         if (this.counter < this.min_count) {
    //             return this.counter
    //         } else {
    //             return this.min_count
    //         }
    //     }
    // }

}
</script>

<style>

</style>