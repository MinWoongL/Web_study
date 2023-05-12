<template>
  <div>
    <h3>뒤로 가기</h3>
    <h1>나중에 볼 비디오</h1>
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
import SearchVideoList from '../SearchView/SearchVideoList.vue'
export default {
    name: "LaterVideoList",
    components: {
      SearchVideoList
    },
    data() {
      return {
        videos: null,
      }
    },
    created() {
      this.$store.dispatch('loadVideos')
      this.videos = this.$store.state.saved_videos
      console.log(this.videos.description)
      
      this.videos.forEach(element => {
        element.description = element.description.slice(0, 100)
      });
    }

}
</script>

<style>

</style>