<template>
  <div id="search">
    <h3>뒤로 가기</h3>
    <h1>{{ video?.title }}</h1>
    <!-- {{ video.upload }} -->
    <br>
    <p>업로드날짜: {{ year }}-{{ month }}-{{ day }}</p>

    <div v-if="url">
      <iframe :src="url" frameborder="0" allowfullscreen width="720px" height="500px"></iframe>
    </div>
    <br>
    <p>{{ video?.description }}</p>
    <div v-if="!isSaved">
      <b-button variant="primary" @click="saveVideo()">동영상 저장</b-button>
    </div>
    <div v-else>
      <b-button variant="success" @click="deleteVideo()">저장 취소</b-button>
    </div>
    

  </div>
</template>

<script>
import axios from 'axios'
export default {
    name: "DetailView",
    data() {
      return {
        video: null,
        year: null,
        month: null,
        day: null,
        url: ''
      } 
    },
    computed: {
      isSaved() {
        if (!this.video) return false
        return this.$store.state.saved_videos.find((item) => {
          return item.id === this.video.id
        }) ? true : false

      }

    },
    created(){
      // https://www.googleapis.com/youtube/v3/videos?part=snippet&id={VIDEO_ID}&key={YOUR_API_KEY}

      // const video = this.$store.getters.get_youtube.find((video) => {
      //   return video.id == this.$route.params.id
      // })
      // this.video = video
      // this.year = this.video.upload.slice(0, 4)
      // this.month = this.video.upload.slice(5, 7)
      // this.day = this.video.upload.slice(8, 10)
      // this.url = `https://www.youtube-nocookie.com/embed/${this.$route.params.id}`
      console.log(this.$route.path)
      this.$store.dispatch('loadVideos')
      this.getFullyoutube()
    },
    methods: {
      getFullyoutube(){
        const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
        axios({
          method: 'get',
          url: `https://www.googleapis.com/youtube/v3/videos`,
          params: {
            key: API_KEY,
            part: 'snippet',
            id: this.$route.params.videoId
          }
        })
        .then((response) => {
          console.log(response)
          const video = response.data.items.map(item => ({
            id: this.$route.params.videoId,
            title: item.snippet.title,
            description: item.snippet.description,
            thumbnail: item.snippet.thumbnails.medium.url,
            upload: item.snippet.publishedAt
          }))
          this.video = video[0]
          this.year = this.video.upload.slice(0, 4)
          this.month = this.video.upload.slice(5, 7)
          this.day = this.video.upload.slice(8, 10)
          this.url = `https://www.youtube-nocookie.com/embed/${this.$route.params.videoId}`
          console.log(this.video)
        })
        .catch((error) => {
          console.log(error)
        })
      },
      saveVideo() {
        this.$store.dispatch('saveVideo', this.video)
      },
      deleteVideo() {
        this.$store.dispatch('deleteVideo', this.video)
      }



    }
    
}
</script>

<style>

</style>