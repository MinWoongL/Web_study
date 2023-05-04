<template>
  <div>
    <h2>결정세액: {{ finalTax }} 만원</h2>
    <button @click="disCount()">클릭 시 10만원 공제</button>
    버튼 클릭 후 세금 : {{ finalTaxData }}
  </div>
</template>

<script>
export default {
  name: 'FinaltaxComponent',
  props: {
    afterTax: Number,
    taxCredit: Number
  },
  data() {
    return {
      finalTaxData: 0,
    }
  },
  computed: {
    finalTax() {
      return this.afterTax - this.taxCredit
    }
  },
  methods: {
    disCount() {
      // computed 속성의 데이터는 직접 변경이 기본적으로는 불가능
      if (this.finalTaxData === 0) {
        this.finalTaxData = this.afterTax - this.taxCredit
      }
      this.finalTaxData -= 10

      // 부모에게 알림!!
      // 부모가 등록한 이벤트인 get-discount 이벤트를 호출
      this.$emit('get-discount', this.finalTaxData)
    }
  },
  beforeCreate() {
    console.log('beforeCreate')
  },
  created() {
    console.log('created')
  },
  beforeMount() {
    console.log('beforeMount')
  },
  mounted() {
    console.log('mounted')
  },
  beforeUpdate() {
    console.log('beforeUpdate')
  },
  updated() {
    console.log('updated')
  },
  beforeDestroy() {
    console.log('beforeDestroy')
  },
  destroyed() {
    console.log('destroyed')
  }
}
</script>

<style>

</style>