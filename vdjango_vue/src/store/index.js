import { createStore } from 'vuex'

export default createStore({
  state: {
    cart: {
      items: [],
    },
    isAuthenticated: false,
    token: '',
    isloading: false
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
})
