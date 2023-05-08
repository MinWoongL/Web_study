<template>
  <div>
    <nav>
      <router-link to="/All">All</router-link> |
      <router-link to="/Important">Important</router-link> |
      <router-link to="/Today">Today</router-link>
    </nav>
    <h2>TodoPageView</h2>
    <router-view/>
  </div>
</template>

<script>

export default {
    name: "TodoPageView",
    data() {
        return {

        }
    }
}
</script>

<style>

</style>