import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    orderList: [],
    menuList: [
      {
        title: '아메리카노',
        price: 3000,
        selected: true,
        image: "<https://source.unsplash.com/featured/?americano>"
      },
      {
        title: '카페라떼',
        price: 4000,
        selected: true,
        image: "<https://source.unsplash.com/featured/?cafelatte>"
      },
      {
        title: '에스프레소',
        price: 10000,
        selected: true,
        image: "<https://source.unsplash.com/featured/?espresso>"
      },
    ],
    sizeList: [
      {
        name: 'grande',
        price: 500,
        selected: true
      },
      {
        name: 'tall',
        price: 1000,
        selected: true
      },
      {
        name: 'venti',
        price: 1500,
        selected: true
      },
    ],
  },
  getters: {
  },
  mutations: {
    addOrder: function () {},
    updateMenuList: function () {},
    updateSizeList: function () {},
  },
  actions: {
  },
  modules: {
  }
})