<template>
  <div class="home">
    <h1>점심메뉴</h1>
    <div>
      <button @click="random_lunch()">Pick Lunch</button>
      <p><b>{{ my }}</b></p>
      <br>
      <h2>로또를 뽑아보자</h2>
      <button @click="toLotto()">Pick Lotto</button>
      <br>
      <button @click="refresh()">새로고침</button>

    </div>
    
  </div>
</template>

<script>
// @ is an alias to /src
// import _ from 'lodash'
export default {
  name: 'TheLunch',
  data() {
    return {
      lunch_menu: ['영양닭죽', '오삼불고기', '치킨샐러드', '성구롤케익', '굶기'],
      my : '메뉴 선택 전'

    }
  },
  components: {
    
  },
  methods: {
    random_lunch() {
      var mymenu = this.lunch_menu[Math.floor(Math.random()*(this.lunch_menu.length))]
      // console.log(mymenu)
      this.my = mymenu
    },
    toLotto() {
      this.$router.push({ name:'Lotto' })
    },
    // 현재페이지에서 현재페이지로 push 요청 시 버그 발생
    // 막아놓은 원인1: 같은 경로 요청 시도 시 성능이 느려짐
    //  원인: 브라우저는 이전 페이지에 대한 정보를 가지고 있음(히스토리)
    //        히스토리에 같은 경로가 또 추가됨
    // 막아놓은 원인2: 동일한 페이지를 여러 번 방문하는 것이 사용자 경험을 저하한다.(사용자 흐름에 방해)
    refresh() {
      // this.$router.push({ name:'Lunch' })  
      location.reload()
      // 경로 사용 시
      // this.$router.push('/lunch').catch(() => {
      //   console.log('같은경로 요청')
      // })
    }
  }
}
</script>
