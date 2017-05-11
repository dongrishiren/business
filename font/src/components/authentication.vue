<template>

  <!-----------------------------用户登入认证模块----------------------------------------->
  <div class="row">
    <div class="col-md-12" v-if="seen_login">
      <el-row class="offset">
        <el-col :span="5" >
          <div style="color: black;font-size:400%">运动世界</div>
        </el-col>
        <el-col :span="3" :offset="15">
          <div class="grid-content bg-purple-dark glyphicon glyphicon-user">
            <router-link :to="{name:'userdetail',params:{'username':$route.params.username}}" style="font-size: x-large;color: black">{{$route.params.username}}</router-link></div>
        </el-col>
        <el-col :span="3" :offset="15">
          <router-link to="/">
            <el-button size="large" type="primary" v-on:click="logout">退出</el-button>
          </router-link>
        </el-col>
      </el-row>
    </div>

    <div class="col-md-12" v-if="seen_logout">
      <el-row class="offset">
        <el-col :span="3" :offset="20">
          <router-link to="/">
            <el-button size="large" type="primary">登入</el-button>
          </router-link>
        </el-col>
        <el-col :span="3" :offset="20">
          <router-link to="/register">
            <el-button size="large" type="warning">注册</el-button>
          </router-link>
        </el-col>
      </el-row>
    </div>
  </div>

</template>
<script>
  import axios from "axios";
  import * as $ from "jquery";
  import "babel-polyfill";
  export default {
 name: 'category_detail',
    data () {
      return {
        seen_login: "",
        seen_logout: "",

      }
    },
    created: function () {
      const vm = this;
      axios.defaults.withCredentials = true;
      const formdata = new FormData();
      formdata.append("from", "8081");
      axios.post(this.host_business+'/business/login_re', formdata, {headers: {"content-type": "", "accept": ""}})
        .then(function (response) {
          if (response.data.status === "200") {
            vm.seen_login = true
          }
          else {
            vm.seen_logout = true
          }
        })
        .catch(function (error) {
          alert(error)
        });
    },
    methods: {
      logout: function () {
        const vm = this;
        const formdata = new FormData();
        formdata.append("from", "8081");
        axios.post(this.host_business+'/business/loginout', formdata, {headers: {"content-type": "", "accept": ""}})
          .then(function (response) {
            if (response.data.status === "200") {
              vm.$router.push({name: 'login'})
            }

          })
          .catch(function (error) {
            alert(error)
          })
      },
    }
  }
</script>
<style>
  .offset {
    margin-top: -2%
  }

  .grid-content {
    color: black;
    font-size: x-large
  }
</style>
