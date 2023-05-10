<template>
  <div>
    <h1>Cat Image</h1>
    <img v-if="imgSrc" :src="imgSrc" alt="">
    <br>
    <button @click="getImage()">Get Cat</button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name: "CatView",
    data() {
        return {
            imgSrc: null,
        }
    },
    computed:{
        myURL() {
            return 'https://api.thecatapi.com/v1/images/search'
        }
    },
    methods: {
        getImage() {
            // const imgURL = 'https://api.thecatapi.com/v1/images/search'
            axios({
                method: 'get',
                url: this.myURL
            })
            .then((response) => {
                console.log(response.data[0].url)
                const imgSrc = response.data[0].url
                this.imgSrc = imgSrc
            })
            .catch((error) => console.log(error))
        },
        
    },
    created(){
        this.getImage()
    }
    

}
</script>

<style>

</style>