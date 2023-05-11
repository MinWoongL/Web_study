<template>
  <div>
    <h5>{{ article.id }}</h5>
    <p>{{ article.title }}</p>
    <hr>
    <router-link
     :to="{
      name: 'DetailView',
      params: { id: article.id }
      }"
    >
      [DETAIL]
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'ArticleListItem',
  props: {
    article: Object,
  }
}
</script>

<style>

</style>
