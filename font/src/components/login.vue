<template>
  <div class="login">
    <link href="../assets/css/bootstrap.min.css">
  <div class="container">
    <div class="row" style="margin-top: 20%">
      <div class="col-md-4 col-md-offset-4 col-xs-8 col-xs-offset-2">
        <h2 class="form-signin-heading">请登录</h2>
        <input type="text" v-model="username"  class="form-control" placeholder="用户名" required autofocus>
        <input type="password" v-model="password" class="form-control" placeholder="密码" required>
        <div class="checkbox">
          <label>
            <input type="checkbox" value="remember-me">
            记住我 </label>
        </div>
        <button class="btn btn-lg btn-primary btn-block" v-on:click="login_">登录</button>
        <div class="row">
          <div class="col-md-6 ">
            <p style="color: red;font-size: small">{{ error }}</p>
          </div>
          <div class="col-md-6 ">
            <router-link to="register" style="font-size: small" >没有账户，注册一个</router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
  </div>
</template>

<script>

  import axios from "axios";
  import "babel-polyfill";
  axios.defaults.withCredentials=true;
  export default {
    name: 'login',
    data () {
      return {
        error:'',
        username: '',
        password: ''
      }
    },
    created:function () {
      document.title = "用户登入";
      const vm = this;
      const formdata = new FormData();
      formdata.append("from", "8081");
      axios.post(this.host_business+'/business/login_re',formdata, {headers:{"content-type":"", "accept":""}})
        .then(function (response) {
          if (response.data.status === "200") {
            vm.$router.push({name:"index",params:{username:response.data.username}})
          }
        })
        .catch(function (error) {
          alert(error)
        })
    },
    methods:{
      login_:function () {
        const vm = this;
        const formdata = new FormData();
        formdata.append("username", vm.username);
        formdata.append("password", vm.password);
        formdata.append("from", "8081");
        axios.defaults.withCredentials=true;
        axios.post(this.host_business+'/business/login_in', formdata,
          {headers: {'Content-Type':'', 'accept':''}})
          .then(function (response) {
            if (response.data.status==="200"){
              vm.$router.push({ name: 'inputinfo', params: { username: vm.username }})
            }
            else if (response.data.status==="211"){
              vm.$router.push({ name: 'index', params: { username: vm.username }})
            }
            else {
              const reg = new RegExp('"', "g");
              vm.error = JSON.stringify(response.data.error).replace(reg, "");
            }

          })
          .catch(function (error) {
            alert(error)
          })
      }
    }
  }

</script>
<style>
  body {
    background: url(../../static/web_media/bg.jpg)fixed no-repeat center;background-size: cover;
  }
</style>
