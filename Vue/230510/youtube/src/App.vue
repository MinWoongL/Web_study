<template>
  <div id="app">
    <h1>SSAFY TUBE</h1>

    <div v-if="url">
      <iframe :src="url" frameborder="0" allowfullscreen width="720px" height="500px"></iframe>
    </div>
    <div id="video-title">
      {{ title }}
    </div>
    <!-- <h2>{{ title }}</h2> -->

  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'App',
  data() {
    return {
      title: '',
      url: ''
    }
  },
  methods: {
    api_call() {
      console.log(process.env)
    },
    get_youtube() {
      const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
      // axios.defaults.withCredentials = true
      axios({
        method: 'get',
        url: 'https://www.googleapis.com/youtube/v3/search',
        params: {
          key: API_KEY,
          part: 'snippet',
          type: 'video',
          q: '코딩노래'
        }
      })
      .then((response) => {
        console.log(response)
        console.log(response.data.items[0].id.videoId)
        // console.log(API_KEY)
        const title = response.data.items[0].snippet.title
        const id = response.data.items[0].id.videoId
        this.title = title
        this.url = `https://www.youtube-nocookie.com/embed/${id}`
      })
      .catch((error) => console.log(error))
    }

  },
  created(){
    this.get_youtube()
  }
}
</script>

<style>
#app {
  font-family: 'Noto Sans KR', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #59a3ec;
  margin-top: 60px;
}
#video-title{
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 25px;
  border: 1px solid gray;
  width: 720px;
  margin-left: 353px; 
  box-shadow: 4px 5px 0px 0px gray;
}

</style>
