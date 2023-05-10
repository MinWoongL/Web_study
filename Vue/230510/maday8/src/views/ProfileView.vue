<template>
  <div>
    <h1>프로필 페이지</h1>

  </div>
</template>

<script>
export default {
    name: "ProfileView",
    data() {
        return {
            isSaved: true,
            username: '',
        }
    },
    // 컴포넌트를 떠나기 전, isSaved 여부에 따라 라우팅을 막기
    beforeRouteLeave(to, from, next) {
        if(this.isSaved){
            console.log(this.isSaved)
            next()
        } else {
            alert('저장하고 나가야함')
            next(false)
        } 
    },
    beforeRouteEnter(to, from, next){
        // 임시적인 비동기 로직
        setTimeout(() => {
            next((comp) => {
                // comp.username = to.params.username
                console.log(comp)

            })
        }, 1000)
    }

}
</script>

<style>

</style>