<template>
  <div class="about">
    <h1>로또</h1>
    <button @click="getLotto()">Get Lucky Numbers</button>
    <p><b>추천 번호 : {{ mynumber }}</b></p>
    <h3>추천 받고 싶은 숫자의 수</h3>
    <input type="text" v-model="count"
    @keyup.enter="getLotto()"
    >
  </div>
</template>

<script>
// import _ from 'lodash'
export default {
  name: "TheLotto",
  data() {
    return {
      mynumber : '',
      count: 6
    }
  },
  methods: {
    getLotto() {
      var myLotto = []
      while(myLotto.length < this.$route.params.count){
        var number = Math.floor(Math.random()*45 + 1)
        myLotto.push(number)
      }
      this.mynumber = myLotto
      this.$router.push(`/lotto/${this.count}`).catch(() => {
        console.log('같은 숫자 입력함!')
      })

    }
  },
  created() {
    console.log(this.$route.params)
  }
}
</script>