<template>
  <div class="home">
    <h2>메인 페이지</h2>
    <div v-if="isLoggedIn">
      <p>반갑습니다! {{ loginUser.id }}님</p>
    </div>
    <div v-else>
      <p>로그인 해주세요! </p>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

import { mapGetters } from 'vuex'
export default {
  name: 'HomeView',
  components: {
    
  },
  computed: {
    loginUser() {
      return this.$store.state.loginUser
    },
    ...mapGetters([
      'isLoggedIn',
    ]),
    // isLoggedIn() {
    //   if(!this.$store.state.loginUser){
    //     return false
    //   }
    //   return true
    // }
  }
}
</script>
