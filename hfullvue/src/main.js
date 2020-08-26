import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

Vue.config.productionTip = false;

//加载highcharts
import HighchartsVue from 'highcharts-vue'
Vue.use(HighchartsVue);

import Highcharts from 'highcharts'
import exportingInit from 'highcharts/modules/exporting'

exportingInit(Highcharts);

// 加载axios
import Axios from 'axios'
Vue.prototype.$axios = Axios;

// 加载css、js
import '@/assets/css/global.css'
import settings from '@/settings'
Vue.prototype.$settings = settings;
import alert from '@/assets/js/test'
Vue.prototype.$alert = alert;

new Vue({
    router,
    store,
    render: h => h(App),
}).$mount('#app');
