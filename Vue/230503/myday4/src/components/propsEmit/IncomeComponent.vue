<template>
<!-- 템플릿 하위에 한개의 태그로만 구성해야 하는것 잊지말기-->
  <div>
    <h1>소득세 계산기</h1>
    <!-- 연봉 입력 -->
    <div>
      <label for="income">연봉 입력 (만원): </label>
      <input type="number" v-model.number="income">

    </div>
    <!-- 세액 감면 -->
    <div>
      <label for="income">세액감면액 (만원): </label>
      <input type="number" v-model.number="taxCredit">

    </div>

    <hr>
    <h2>종합소득금액 : {{ income }}만원</h2>
    <h2>종합소득공제 : (-) 150만원</h2>
    <h2>과세표준 : {{ taxBaseCal }}만원</h2>
    <h2>버튼 클릭 후 세금: {{ finalTax }}</h2>
    <hr>
    <!-- 부모컴포넌트에서 넘겨줄 때 -->
    <!-- kebab-case 형태로 변수명 = "넘겨줄인자" -->
    <TaxrateComponent
    :my-income="taxBaseCal"
    :my-taxcredit="notStrtaxcredit"
    @get-discount="getDisCount"
    />

  </div>
</template>

<script>
import TaxrateComponent from './TaxrateComponent.vue'
export default {
  name: 'IncomeComponent',
  components: {
    TaxrateComponent
  },
  // props:{
  //   myIncome: {
  //     type: Number,
  //     default: 0
  //   }
  // },
  computed: {
    taxBaseCal() {
      // 삼항연산자로 표현할 수 있음
      // return this.income - 150 >= 0 ? this.income - 150 : 0
      let taxBase = this.income - 150
      if (taxBase <= 0) {
        return 0
      } else {
        return taxBase
      }
    },
    notStrtaxcredit() {
      if (this.taxCredit === "") {
        return 0
      } else {
        return this.taxCredit
      }
    }
  },
  data() {
    return {
      income: "",
      taxCredit: "",
      finalTax: 0,
    }
  },
  methods: {
    getDisCount(finalTax) {
      console.log('자식에게서의 호출')
      console.log(`자식이 보낸 데이터: ${finalTax}`)
      this.finalTax = finalTax
    }
  }
}
</script>

<style>

</style>