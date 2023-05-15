<template>
  <div>
    <h1>Article Page</h1>
    <router-link :to="{ name: 'CreateView' }">[CREATE]</router-link>
    <ArticleList />
    <hr>
  </div>
</template>

<script>
import ArticleList from '@/components/ArticleList.vue'

export default {
  name: 'ArticleView',
  components: {
    ArticleList,
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles() {
      if(this.isLogin) {
        this.$store.dispatch('getArticles')
      } else {
        alert('로그인이 필요한 서비스 입니다.')
        this.$router.push({ name: 'LogInView' })
      }
      
    }
  }
}
</script>

<style>

</style>
