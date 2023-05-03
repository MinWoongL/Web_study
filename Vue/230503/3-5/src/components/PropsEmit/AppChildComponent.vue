<template>
  <div>
    <h2>AppChild</h2>
    <input type="text" v-model.number="childData" @input="postchildData">
    <br>
    <p>appData: {{myAppdata}}</p>
    <p>parentData: {{myParentdata}}</p>
    <p>childData: {{childData}}</p>
  </div>
</template>

<script>
export default {
    name: "AppChildComponent",
    data() {
        return {
            childData: 0,
        }
    },
    props: {
        myParentdata: Number,
        myAppdata: Number
    },
    methods: {
        postchildData() {
            this.$emit('get-childdata', this.childData)
        }

    }

}
</script>

<style>

</style>