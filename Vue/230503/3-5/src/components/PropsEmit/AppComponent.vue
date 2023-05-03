<template>
  <div>
    <h2>App</h2>
    <input type="text" v-model.number="appData">
    <br>
    <p>parentData: {{ getPdata }}</p>
    <p>childData: {{ getCdata }}</p>
    <hr>
    <AppParentComponent
    :my-appdata="notstrAppdata"
    @get-parentdata="getParentdata"
    @get-child-data="getChildData"
    />
  </div>
</template>

<script>
import AppParentComponent from './AppParentComponent.vue'
export default {
    name: "AppComponent",
    components: {
        AppParentComponent
    },
    data() {
        return {
            appData: 0,
            getPdata: 0,
            getCdata: 0,
        }
    },
    methods: {
        getParentdata(data) {
            this.getPdata = data
        },
        getChildData(data) {
            this.getCdata = data
        }
    },
    computed: {
        notstrAppdata() {
            if (this.appData === '') {
                return 0
            } else {
                return this.appData
            }
        }
    }

}
</script>

<style>

</style>