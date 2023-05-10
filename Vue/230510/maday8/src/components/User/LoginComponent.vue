<template>
  <div>
    <h2>난 로그인 컴포넌트</h2>
    <hr>
    <div>
      <label for="id">ID</label>
      <input type="text" v-model="form.id">
    </div>
    <br>
    <div>
      <label for="pw">PW</label>
      <input type="text" v-model="form.pw">
    </div>
    <br>
    <button @click="login()">로그인</button>
  </div>
</template>

<script>
export default {
    name: "LoginComponent",
    data() {
      return {
        form: {
          id: '',
          pw: '',
        }
      }
    },
    methods: {
      login() {
        // 최소한의 유효성 검증
        if(this.form.id === ''){
          alert('ID를 입력하세요')
          return
        }
        if(this.form.pw === ''){
          alert('PW를 입력하세요')
          return
        }
        // 모두 정상적인 입력이라면, action dispatch
        
        // dispatch 도 promise 객체를 반환한다 -> .then, .catch 사용가능
        this.$store.dispatch('login', this.form).then(() => {
          this.$router.push('/')
        }).catch((error) => {
          console.log(error)
        })
      }
    }

}
</script>

<style>

</style>