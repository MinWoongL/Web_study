<template>
  <div>
    <h2>산출세액 : {{ taxCal }} 만원</h2>
    <h2>세액감면 : (-) {{ myTaxcredit }} 만원</h2>
    <h2>버튼 클릭 후 세금: {{ finalTax }}</h2>
    <hr>
    <FinaltaxComponent
    :result-tax="resultTax"
    @get-discount="getDisCount"
    />

  </div>
</template>

<script>
import FinaltaxComponent from './FinaltaxComponent.vue'

export default {
  name: 'TaxrateComponent',
  data() {
    return {
      finalTax: 0,
    }
  },
  components: {
    FinaltaxComponent
  },
  props: {
    // 자식컴포넌트에서 받을때
    // camelCase 형태로 부모컴포넌트에서 넘겨준 인자를 받는다.
    myIncome:{
      type: Number,
      default: 0
    },
    myTaxcredit: Number
  },
  computed: {
    taxCal() {
      if (this.myIncome<=1200) {
        return Math.ceil(this.myIncome*0.06)
      } else if (this.myIncome <= 4600) {
        return Math.ceil((this.myIncome*0.15 - 108))
      } else if (this.myIncome <= 8800) {
        return Math.ceil(this.myIncome*0.24 - 522)
      } else if (this.myIncome <= 15000) {
        return Math.ceil(this.myIncome*0.35 - 1490)
      } else if (this.myIncome <= 30000) {
        return Math.ceil(this.myIncome*0.38 - 1940)
      } else if (this.myIncome <= 50000) {
        return Math.ceil(this.myIncome*0.40 - 2540)
      } else if (this.myIncome <= 100000) {
        return Math.ceil(this.myIncome*0.42 - 3540)
      }else {
        return Math.ceil(this.myIncome*0.45 - 6540)
      }
    },
    resultTax() {
      return this.taxCal - this.myTaxcredit
    }
  },
  methods: {
    getDisCount(final) {
      console.log('자식에게서의 호출')
      console.log(`자식이 보낸 데이터: ${final}`)
      this.finalTax = final
      // 부모에게 자식의 데이터를 전달
      this.$emit('get-discount', final)
    }
  }

}
</script>

<style>

</style>