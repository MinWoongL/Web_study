<template>
  <div>
      <b-card :img-src="video.thumbnail" :img-alt="video.title" img-top @click="goDetail()">
        <b-card-title>{{ video.title }}</b-card-title>
        <b-card-text>{{ video.description }}</b-card-text>
      </b-card>
  </div>
</template>

<script>
export default {
    name: "SearchVideoList",
    props: {
        video: Object
    },
    methods: {
      goDetail() {
        this.$router.push({name: "video_detail", params:{videoId: this.video.id}})
      }
    }
}
</script>

<style>

</style>