<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <!-- 3. 사용한다. -->
    <MyComponent/>
    <HelloWorld msg="msg 텍스트만 바꿔보자"/>
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <p>HEADER</p>
    <HomeView/>
    <p>FOOTER</p>

  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
// @로 쓸 수도 있다. -> @는 src 폴더를 의미
// import MyComponent from '@/components/MyComponent.vue'
import MyComponent from './components/MyComponent.vue' // 1.불러온다.
import HomeView from './views/HomeView.vue'


export default {
  name: 'App',
  components: {
    HelloWorld,
    MyComponent, // 2. 등록한다.
    HomeView,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
