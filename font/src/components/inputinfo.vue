<template>
  <div class="inputinfo">
    <auth></auth>
        <el-row>
      <el-col :span="8" :offset="8"><h2>请录入个人信息</h2></el-col>
    </el-row>
    <el-row class="offset2">
      <el-col :span="4" :offset="10" v-for="(num, index) in nums">
        <el-input v-model="value_list[index]" v-bind:placeholder=num size="large">
          <template slot="prepend">
            <div class="name">{{num}}</div>
          </template>
        </el-input>
      </el-col>
    </el-row>
    <div class="offset3">
      <el-button type="primary" size="large" v-on:click="postinfo">确认信息</el-button>
      <p style="color: red">{{info}}</p>
    </div>
  </div>
</template>
<script>
  import axios from "axios";
  import * as $ from "jquery";
  import "babel-polyfill";
  import ElButton from "../../node_modules/element-ui/packages/button/src/button";
  import auth from "./authentication.vue"
  export default{
    components: {ElButton, "auth":auth},
    data(){
      return {
          info:"",
        value_list: ["", "", "", "", "", ""],
        nums: ["姓名", "电话", "性别", "年龄", "邮箱", "爱好"],
      }
    },
    created:function () {
      document.title = "欢迎来到运动世界"
    },
    methods: {
      postinfo: function () {
        const vm = this;
        const formdata = new FormData();
        formdata.append("from", "8081");
        formdata.append("username", vm.$route.params.username);
        formdata.append("name", vm.value_list[0]);
        formdata.append("phone", vm.value_list[1]);
        formdata.append("sex", vm.value_list[2]);
        formdata.append("old", vm.value_list[3]);
        formdata.append("mail", vm.value_list[4]);
        formdata.append("interest", vm.value_list[5]);
        axios.post(this.host_business+'/business/save_user_info', formdata, {headers: {"content-type": "", "accept": ""}})
          .then(function (response) {
            if (response.data.status === "200") {
              vm.$router.push({ name: 'index', params: { username: vm.$route.params.username }})
            }
            else {
                vm.info =JSON.stringify(response.data.info)
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
  .name {
    color: black;
    font-weight: 900
  }

  .offset2 {
    margin-top: 1%
  }

  .offset3 {
    margin-top: 2%
  }

  .log {
    font-size: 600%;
    color: black;
    font-weight: 500;
  }
</style>
