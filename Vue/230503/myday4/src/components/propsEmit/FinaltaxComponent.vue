<template>
  <div>
    <h2>결정세액 : {{resultCal}} 만원</h2>
    <button @click="disCount()">클릭 시 10만원 공제</button>
  </div>
</template>

<script>
export default {
  name: 'FinaltaxComponent',
  props: {
    resultTax: Number
  },
  data() {
    return {
      final: 0,
    }
  },
  computed: {
    resultCal() {
      if (this.resultTax < 0) {
        return 0
      } else {
        return this.resultTax
      }
    }
  },
  methods: {
    disCount() {
      // computed 속성의 데이터는 직접 변경이 불가능
      if (this.final === 0) {
        this.final = this.resultTax
      } else {
        this.final -= 10
      }
      // 부모가 등록한 이벤트인 get-discount 이벤트를 호출

      this.$emit('get-discount', this.final)
    }
  }
}
</script>

<style>

</style>