import Vue from 'vue'
import Router from 'vue-router'
import dynamic from './views/dynamic.vue'
import backupShow from './views/backupShow.vue'
import show from './views/show.vue'

Vue.use(Router);

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'dynamic',
            component: dynamic
        },
        {
            path: '/backup',
            name: 'backupShow',
            component: backupShow
        },
        {
            path: '/backup1',
            name: 'dataShow',
            component: show
        },
    ]
})
