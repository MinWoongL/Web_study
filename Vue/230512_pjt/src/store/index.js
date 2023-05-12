import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const YOUTUBE_URL = 'https://www.googleapis.com/youtube/v3/search'

export default new Vuex.Store({
  state: {
    videos: [

    ],
    // 나중에 볼 동영상 저장 할 리스트
    saved_videos: [

    ]
  },
  getters: {
    get_youtube(state) {
      return state.videos
    }

  },
  mutations: {
    GET_YOUTUBE(state, videos) {
      console.log(videos)
      state.videos = videos
    },
    SAVE_VIDEO(state, video) {
      state.saved_videos.push(video)
    },
    DELETE_VIDEO(state, video) {
      const id = state.saved_videos.indexOf(video)
      state.saved_videos.splice(id, 1)
    },
    LOAD_VIDEOS(state){
      const localStorageVideos = localStorage.getItem('savedVideos')
      // 내 로컬스토리지에 데이터가 있었을 경우만 saved_videos에 넣어주기
      if (localStorageVideos) {
        state.saved_videos = JSON.parse(localStorageVideos)
      }
    }
  },
  actions: {
    getYoutube(context, search){
      axios({
        method: 'get',
        url: YOUTUBE_URL,
        params: {
          key: API_KEY,
          part: 'snippet',
          type: 'video',
          maxResults: 9,
          q: search
        }
      })
      .then((response) => {
        console.log(response.data)
        // console.log(response.data.items[0].id.videoId)
        // console.log(response.data.items[0].snippet.title)
        const videos = response.data.items.map(item => ({
          id: item.id.videoId,
          title: item.snippet.title,
          description: item.snippet.description,
          thumbnail: item.snippet.thumbnails.medium.url,
          upload: item.snippet.publishedAt
        }))
        context.commit('GET_YOUTUBE', videos)
      })
      .catch((error) => {
        console.log(error)
      })
      
    },
    loadVideos(context){
      context.commit('LOAD_VIDEOS')
    },
    // 저장, 삭제 시 로컬스토리지도 바꿔줄 수 있도록 saveVideoToLocalStorage 호출
    saveVideo(context, video){
      context.commit('SAVE_VIDEO', video)
      context.dispatch('saveVideoToLocalStorage')
    },
    deleteVideo(context, video){
      context.commit('DELETE_VIDEO', video)
      context.dispatch('saveVideoToLocalStorage')
    },
    saveVideoToLocalStorage(context) {
      // 로컬스토리지는 문자열 밖에 인식 못함
      // JSON.stringify => 문자열로 반환
      const jsonVideos = JSON.stringify(context.state.saved_videos)
      localStorage.setItem('savedVideos', jsonVideos)
    },
    
  },
  modules: {
  }
})
