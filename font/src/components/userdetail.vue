<template class="body">
  <div class="userdetail">
    <auth></auth>
    <el-tabs v-model="activeName2" type="card" @tab-click="handleClick">
      <el-tab-pane label="购买清单" name="first"><h1>购买清单</h1></el-tab-pane>
      <el-tab-pane label="用户资料" name="second"><h1>用户资料</h1></el-tab-pane>
      <el-tab-pane label="更新通告" name="third"><h1>更新通告</h1></el-tab-pane>
    </el-tabs>

    <div v-if="userinfo">
      <el-table
        :data="userInfo"
        border
        style="width: 50%;margin:0 auto">
        <el-table-column
          prop="name"
          label="姓名">
        </el-table-column>
        <el-table-column
          prop="phone"
          label="电话">
        </el-table-column>
        <el-table-column
          prop="sex"
          label="性别">
        </el-table-column>
        <el-table-column
          prop="old"
          label="年龄">
        </el-table-column>
        <el-table-column
          prop="mail"
          label="邮箱">
        </el-table-column>
        <el-table-column
          prop="interest"
          label="爱好">
        </el-table-column>
      </el-table>
    </div>

    <div v-if="order">
      <el-table
        :data="tableData"
        border
        style="width: 80%;margin:0 auto"
        :default-sort="{prop: 'date', order: 'descending'}">
        <el-table-column
          fixed
          prop="date"
          label="日期"
          sortable>
        </el-table-column>
        <el-table-column
          prop="category"
          label="种类"
          sortable>
        </el-table-column>
        <el-table-column
          prop="info"
          label="产品名称"
          sortable>
        </el-table-column>
        <el-table-column
          prop="detail"
          label="产品详情"
          sortable>
        </el-table-column>
        <el-table-column
          prop="image"
          label="产品图片"
          sortable>
        </el-table-column>
        <el-table-column
          prop="price"
          label="价格"
          sortable>
        </el-table-column>

        <el-table-column
          fixed="right"
          label="操作"
          width="100">
          <template scope="scope">
            <router-link
              :to="{name:'product_info', params:{'username':'admin','back_user': 'admin','info':'板鞋','num':'2'}}">查看
            </router-link>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>
<script>
  import axios from "axios";
  import "babel-polyfill";
  import auth from "./authentication.vue"
  export default {
      components:{"auth":auth},
    name: "userdetail",
    data() {
      return {
        activeName2: 'first',
        order: true,
        userinfo: "",
        ad: "",
        tableData: [{
          date: '2016-05-03',
          info: '轻巧跑步板鞋',
          detail: '让你跑的像风一样',
          image: '...',
          price: '123',
          category: '板鞋'
        },],
        userInfo: "",
      };
    },
    created: function () {
      document.title = "用户数据";
      const formdata = new FormData();
      const vm = this;
      formdata.append("from", "8081");
      formdata.append("user", this.$route.params.username);
      axios.post(this.host_business+'/business/get_userinfo', formdata,
        {headers: {'Content-Type': 'application/form-data'}, withCredentials: false})
        .then(function (response) {
          if (response.data.status === "200") {
            const list_ = [];
            const name = response.data.info.match(/'name': '(\S*)'/)[1];
            const old = response.data.info.match(/'old': (\S*),/)[1];
            const phone = response.data.info.match(/'phone': '(\S*)'/)[1];
            const mail = response.data.info.match(/'mail': '(\S*)'/)[1];
            const sex = response.data.info.match(/'sex': '(\S*)'/)[1];
            const interest = response.data.info.match(/'interest': '(\S*)'/)[1];
            vm.userInfo = [{"name":name,"old":old,"phone":phone,"mail":mail,"interest":interest,"sex":sex},];
          }
          else {

          }
        })
        .catch(function (error) {
          alert(error)
        });

    },
    methods: {
      handleClick(tab, event) {
        if (this.activeName2 === "first") {
          this.order = true;
          this.userinfo = "";
          this.ad = ""
        }
        if (this.activeName2 === "second") {
          this.order = "";
          this.userinfo = true;
          this.ad = ""
        }
        if (this.activeName2 === "third") {
          this.order = "";
          this.userinfo = "";
          this.ad = true
        }
      }
    }
  };
</script>

