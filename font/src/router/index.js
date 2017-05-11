import Vue from 'vue'
import Router from 'vue-router'
import login from '../components/login.vue'
import index from '../components/index.vue'
import register from '../components/register.vue'
import category_detail from '../components/category_detail.vue'
import category from '../components/category.vue'
import product_info from '../components/product_info.vue'
import userdetail from '../components/userdetail.vue'
import inputinfo from '../components/inputinfo.vue'

Vue.use(Router);


export default new Router({
  mode:"history",
  routes: [
    {
      path: '/',
      name: 'login',
      component: login
    },
    {
      path: '/index/:username',
      name: 'index',
      component: index
    },
    {
      path: '/register',
      name: 'register',
      component: register
    },
    {
      path: '/category/:username/:category',
      name: 'category',
      component: category
    },
    {
      path: '/category_detail/:username/:category',
      name: 'category_detail',
      component: category_detail
    },
    {
      path: '/product_info/:username/:back_user/:info/:num',
      name: 'product_info',
      component: product_info
    },
    {
      path: '/userdetail/:username',
      name: 'userdetail',
      component: userdetail
    },
    {
      path: '/inputinfo/:username',
      name: 'inputinfo',
      component: inputinfo
    },
  ]
})
