import Vue from 'vue'
import App from './App.vue'
import router from './router'
import Axios from 'axios'


// const token = localStorage.getItem("jwt");
// Axios.defaults.headers.common["Authorization"] = `Bearer ${token}`
// Vue.prototype.$http = Axios

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
