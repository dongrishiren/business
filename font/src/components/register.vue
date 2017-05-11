<template>

  <div class="register">
    <link href="../assets/css/bootstrap.min.css">
  <div class="container">
    <div class="row" style="margin-top: 20%">
      <div class="col-md-4 col-md-offset-4 col-xs-8 col-xs-offset-2">
        <h2 class="form-signin-heading">请注册</h2>
        <input type="text" v-model="username"  class="form-control" placeholder="用户名" required autofocus>
        <input type="password" v-model="password" class="form-control" placeholder="密码" required>
        <div class="checkbox">
          <label>
            <input type="checkbox" value="remember-me">
            记住我 </label>
        </div>
        <button class="btn btn-lg btn-danger btn-block" v-on:click="register_">注册</button>
        <div class="row">
          <div class="col-md-6 ">
            <p style="color: red;font-size: small">{{ error }}</p>
          </div>
          <div class="col-md-6 ">
            <router-link to="/" style="font-size: small" >已有账户，直接登入</router-link>
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
  export default {
    name: 'register',
    data () {
      return {
        error:'',
        username: '',
        password: ''
      }
    },
    created:function () {
      document.title = "用户注册"
    },
    methods:{
      register_:function () {
        const vm = this;
        const formdata = new FormData();
        formdata.append("username", vm.username);
        formdata.append("password", vm.password);
        formdata.append("from", "8081");
        axios.defaults.withCredentials=true;
        axios.post(this.host_business+'/business/register_in', formdata,
          {headers: {'Content-Type':'', 'accept':''}, withCredentials:false})
          .then(function (response) {
              const reg = new RegExp('"', "g");
              vm.error = JSON.stringify(response.data.error).replace(reg, "");

          })
          .catch(function (error) {
            alert(error)
          })
      }
    }
  }

</script>

