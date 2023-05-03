<template>
  <div>
    <h2>AppParent</h2>
    <input type="text" v-model.number="parentData" @input="postParentdata">
    <br>
    <p>appData: {{myAppdata}}</p>
    <p>childData: {{childComponentData}}</p>
    <hr>
    <AppChildComponent
    :my-appdata="myAppdata"
    :my-parentdata="notstrParentData"
    @get-childdata="getChilddata"
    />

  </div>
</template>

<script>
import AppChildComponent from './AppChildComponent.vue'

export default {
    name: "AppParentComponent",
    components: {
        AppChildComponent
    },
    data() {
        return {
            parentData: 0,
            childComponentData: 0,
        }
    },
    props: {
        myAppdata: Number
    },
    methods: {
        getChilddata(data) {
            this.childComponentData = data
            this.$emit('get-child-data', this.childComponentData)
        },
        postParentdata() {
            this.$emit('get-parentdata', this.parentData)
        }
    },
    computed: {
        notstrParentData() {
            if (this.parentData === '') {
                return 0
            } else {
                return this.parentData
            }
        }
    }


}
</script>

<style>

</style>