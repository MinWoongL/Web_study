<template>
  <div>
    <h1>비디오 검색</h1>
    <b-form @submit.prevent="searchVideos" class="mb-4">
      <div class="bv-example-row">
        <b-row>
          <b-col cols="10">
            <b-form-input v-model="search" placeholder="검색어를 입력하세요"></b-form-input>
          </b-col>
          <b-col>
            <b-button type="submit" variant="success" class="text-center"
              @click="getyoutube()"
            >찾기</b-button>
          </b-col> 
        </b-row>
      </div>
    </b-form>
    <div v-if="!videos">
      <p>로딩 중</p>
    </div>
    <b-row v-else>
      <b-col cols="4" v-for="video in videos" :key="video.id">
        <SearchVideoList
          :video = "video"/>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import SearchVideoList from '@/components/SearchView/SearchVideoList.vue'
export default {
    name: "SearchInput",
    components: {
      SearchVideoList
    },
    data() {
      return {
        search: '',
      }
    },
    computed: {
      videos() {
        return this.$store.state.videos.length === 0 ? false : this.$store.state.videos
      }

    },
    methods: {
      searchVideos() {
        console.log('test')
      },
      getyoutube() {
        this.$store.dispatch('getYoutube', this.search)
      }
      
    },
    created(){
      console.log(this.$route)
      console.log(this.$route.path)
    }

}
</script>

<style >
    #search {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: start;
        margin: 50px 100px 0px 100px;
        color: #2c3e50;
    }


</style>