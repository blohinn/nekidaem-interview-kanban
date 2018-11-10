import Vue from 'vue'
import Cookies from 'js-cookie'

import router from './router'
import {store} from './store'

Vue.config.productionTip = false;
Vue.prototype.$cookies = Cookies;

import App from './App'


new Vue({
  el: '#app',
  store,
  router,
  render: h => h(App)
});
