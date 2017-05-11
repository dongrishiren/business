<template xmlns:v-on="http://www.w3.org/1999/xhtml" xmlns:v-bind="http://www.w3.org/1999/xhtml">

  <div class="category_detail">
    <auth></auth>
    <link href="../assets/css/bootstrap.min.css">
    <div class="jumbotron" style="background: transparent;margin-top: -5%">
      <div class="container">

        <div class="row">
          <div class="col-md-4" v-for="category in categorys">
            <button class="btn btn-lg btn-block btn-primary" v-on:click="change_title1">{{category}}</button>
          </div>
          <p style="margin-top: 5%">  </p>
          <div v-if="shoe_ca">
          <div class="col-md-4" v-for="categorys_shoe in categorys_shoes">
            <button class="btn btn-lg btn-block btn-success" v-on:click="change_title2">{{categorys_shoe}}</button>
          </div>
          </div>
          <div v-if="clothes_ca">
          <div class="col-md-4" v-for="categorys_clothe in categorys_clothes">
            <button class="btn btn-lg btn-block btn-success" v-on:click="change_title2">{{categorys_clothe}}</button>
          </div>
          </div>
          <div v-if="tools_ca">
          <div class="col-md-4" v-for="categorys_tool in categorys_tools">
            <button class="btn btn-lg btn-block btn-success" v-on:click="change_title2">{{categorys_tool}}</button>
          </div>
          </div>
        </div>
      </div>

      <div v-if="shoe_ca">
        <div class="container">
          <div class="row " style="margin-top: auto">
            <div v-for="(shoesinfo,index) in (shoesinfos)">
              <div class="col-md-4">
                <h2 align="center">{{shoesinfo}}</h2>
                <img v-bind:src=new_src_images[index] style="width: 100%;">
                <router-link :to="{ name: 'product_info', params: { 'back_user': users_[index],'info':shoesinfo,'num':'2' }}"
                             class="btn btn-primary btn-lg" style="width:40%;" role="button">
                  了解更多
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>

            <div v-if="clothes_ca">
        <div class="container">
          <div class="row " style="margin-top: auto">
            <div v-for="(clothesinfo,index) in (clothesinfos)">
              <div class="col-md-4">
                <h2 align="center">{{clothesinfo}}</h2>
                <img v-bind:src=new_src_images_clothes[index] style="width: 100%;">
                <router-link :to="{ name: 'product_info', params: { 'back_user': users_[index],'info':clothesinfo,'num':'1' }}"
                             class="btn btn-primary btn-lg" style="width:40%;" role="button">
                  了解更多
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>


            <div v-if="tools_ca">
        <div class="container">
          <div class="row " style="margin-top: auto">
            <div v-for="(toolsinfo,index) in (toolsinfos)">
              <div class="col-md-4">
                <h2 align="center">{{tollsinfo}}</h2>
                <img v-bind:src=new_src_images_tools[index] style="width: 100%;">
                <router-link :to="{ name: 'product_info', params: { 'back_user': users_[index],'info':toolsinfo,'num':'3' }}"
                             class="btn btn-primary btn-lg" style="width:40%;" role="button">
                  了解更多
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>


    </div>

    <p style="margin-top: 5%"></p>
  </div>


</template>

<script>
  import axios from "axios";
  import * as $ from "jquery";
  import "babel-polyfill";
  import auth from "./authentication.vue"
  function get_catdetail(category, users, images) {
    const long = users.split("', '").length;
            if (long>=2){

            const users_ = users.split("', '");
            const categorys = category.split("', '");
            const src_images = images.split(">, <FieldFile: ");
            categorys.splice(0, 1);
            categorys.unshift(category.split("', '")[0].match(/\['(\S*)/)[1]);
            categorys.splice(-1, 1);
            categorys.push(category.split("', '")[long-1].match(/(\S*)']/)[1]);
            src_images.splice(0, 1);
            src_images.unshift(images.split(">, <FieldFile: ")[0].match(/\[<FieldFile: (\S*)/)[1]);
            src_images.splice(-1, 1);
            src_images.push(images.split(">, <FieldFile: ")[long-1].match(/(\S*)>]/)[1]);
            const new_src_images = [];
            const len = src_images.length;
              for (let i = 0; i < parseInt(len); i++) {
              new_src_images.push(src_images[i].split("font")[1])
            }
            users_.splice(0, 1);
            users_.unshift(users.split("', '")[0].match(/\['(\S*)/)[1]);
            users_.splice(-1, 1);
            users_.push(users.split("', '")[long-1].match(/(\S*)']/)[1]);
            return [new_src_images, users_, categorys]

            }
            if (users!=='[]'){
                const new_src_images = [];
                new_src_images.push(images.match(/\[<FieldFile: font(\S*)>]/)[1]);
                const users_ = [];
                users_.push(users.match(/\['(\S*)']/)[1]);
                const infos = [];
                infos.push(category.match(/\['(\S*)']/)[1]);
                return [new_src_images, users_, infos]
            }
            else {
                return [[],[],[]]
            }
  }
  export default {
    components: {"auth":auth},
    name: 'category_detail',
    data () {
      return {
        categorys: ["服饰", "鞋类", "配件"],
        categorys_shoes: ["板鞋", "篮球鞋", "跑鞋", "网鞋", "帆布鞋", "羽毛球鞋", "足球鞋", "拖鞋", "凉鞋",],
        categorys_clothes: ["夏季男装", "夏季女装", "冬季男装", "冬季女装",],
        categorys_tools: ["球类配件", "袜子", "箱包", "手脚护腕", "眼镜"],
        users_: [],
        new_src_images: [],
        new_src_images_clothes: [],
        new_src_images_tools: [],
        shoesinfos: [],
        clothesinfos:[],
        toolsinfos:[],
        src_images: [],
        shoe_ca: true,
        clothes_ca: "",
        tools_ca: "",
        error: '',
        password: '',
        interface_:"",
      }
    },
    created: function () {
      const vm = this;
      document.title = "运动世界商城";

      if($.inArray(this.$route.params.category, ["板鞋", "篮球鞋", "跑鞋", "网鞋", "帆布鞋", "羽毛球鞋", "足球鞋", "拖鞋", "凉鞋",])>=0){
                formdata.append("category", this.$route.params.category);
      axios.post(this.host_business+'/business/get_business_info', formdata, {
        headers: {
          "content-type": "",
          "accept": ""
        }, withCredentials: false
      })
        .then(function (response) {
          if (response.data.status === "200") {
              [vm.new_src_images, vm.users_, vm.shoesinfos ] = get_catdetail(response.data.shoesinfo,
                                                                              response.data.user,
                                                                              response.data.image);

          }
          else {
            vm.$router.push({name: 'login'})
          }
        })
        .catch(function (error) {
          alert(error)
        });
        this.interface_="2";
        this.shoe_ca = true;
        this.clothes_ca = "";
        this.tools_ca = "";
        return
      }
      if($.inArray(this.$route.params.category, ["夏季男装", "夏季女装", "冬季男装", "冬季女装",])>=0){

formdata.append("category", this.$route.params.category);
      axios.post(this.host_business+'/business/get_business_info_clothes', formdata, {
        headers: {
          "content-type": "",
          "accept": ""
        }, withCredentials: false
      })
        .then(function (response) {
          if (response.data.status === "200") {
            [vm.new_src_images_clothes, vm.users_, vm.clothesinfos ] = get_catdetail(response.data.clothesinfo,
                                                                              response.data.user,
                                                                              response.data.image);

          }
          else {
            vm.$router.push({name: 'login'})
          }
        })
        .catch(function (error) {
          alert(error)
        });
        this.interface_="1";
        this.shoe_ca = "";
        this.clothes_ca = true;
        this.tools_ca = "";
        return
      }
      if($.inArray(this.$route.params.category, ["球类配件", "袜子", "箱包", "手脚护腕", "眼镜"])>=0){
formdata.append("category", this.$route.params.category);
      axios.post(this.host_business+'/business/get_business_info_tools', formdata, {
        headers: {
          "content-type": "",
          "accept": ""
        }, withCredentials: false
      })
        .then(function (response) {
          if (response.data.status === "200") {
            [vm.new_src_images_tools, vm.users_, vm.toolsinfos ] = get_catdetail(response.data.toolsinfo,
                                                                              response.data.user,
                                                                              response.data.image);
          }
          else {
            vm.$router.push({name: 'login'})
          }
        })
        .catch(function (error) {
          alert(error)
        });
        this.interface_="3";
        this.shoe_ca = "";
        this.clothes_ca = "";
        this.tools_ca = true;
      }

    },
    methods: {
      change_title1: function (event) {
          const vm = this;
        if (event.target.innerHTML==="服饰") {
            const formdata = new FormData();
      formdata.append("from", "8081");
      formdata.append("category", "夏季男装");
      axios.post(this.host_business+'/business/get_business_info_clothes', formdata, {
        headers: {
          "content-type": "",
          "accept": ""
        }, withCredentials: false
      })
        .then(function (response) {
          if (response.data.status === "200") {
            [vm.new_src_images_clothes, vm.users_, vm.clothesinfos ] = get_catdetail(response.data.clothesinfo,
                                                                              response.data.user,
                                                                              response.data.image);
          }
          else {
            vm.$router.push({name: 'login'})
          }
        })
        .catch(function (error) {
          alert(error)
        });
            this.interface_="1";
            this.shoe_ca = "";
            this.clothes_ca = true;
            this.tools_ca = "";
            return

        }
        if (event.target.innerHTML==="鞋类") {
            const vm = this;
                  const formdata = new FormData();
      formdata.append("from", "8081");
      formdata.append("category", "板鞋");
      axios.post(this.host_business+'/business/get_business_info', formdata, {
        headers: {
          "content-type": "",
          "accept": ""
        }, withCredentials: false
      })
        .then(function (response) {
          if (response.data.status === "200") {
            [vm.new_src_images, vm.users_, vm.shoesinfos ] = get_catdetail(response.data.shoesinfo,
                                                                              response.data.user,
                                                                              response.data.image);
          }
          else {
            vm.$router.push({name: 'login'})
          }
        })
        .catch(function (error) {
          alert(error)
        });
            this.interface_="2";
            this.shoe_ca = true;
            this.clothes_ca = "";
            this.tools_ca = "";
            return
        }
        if (event.target.innerHTML==="配件") {
            const vm = this;
          const formdata = new FormData();
      formdata.append("from", "8081");
      formdata.append("category", "球类配件");
      axios.post(this.host_business+'/business/get_business_info_tools', formdata, {
        headers: {
          "content-type": "",
          "accept": ""
        }, withCredentials: false
      })
        .then(function (response) {
          if (response.data.status === "200") {
            [vm.new_src_images_tools, vm.users_, vm.toolsinfos ] = get_catdetail(response.data.toolsinfo,
                                                                              response.data.user,
                                                                              response.data.image);
          }
          else {
            vm.$router.push({name: 'login'})
          }
        })
        .catch(function (error) {
          alert(error)
        });
            this.interface_="3";
            this.shoe_ca = "";
            this.clothes_ca = "";
            this.tools_ca = true;
        }
      },
      change_title2: function (event) {
          const vm = this;
      const formdata = new FormData();
      formdata.append("from", "8081");
      formdata.append("category", event.target.innerHTML);
      if(this.interface_==="1"){
      axios.post(this.host_business+'/business/get_business_info_clothes', formdata, {
        headers: {
          "content-type": "",
          "accept": ""
        }, withCredentials: false
      })
        .then(function (response) {
          if (response.data.status === "200") {
            [vm.new_src_images_clothes, vm.users_, vm.clothesinfos ] = get_catdetail(response.data.clothesinfo,
                                                                              response.data.user,
                                                                              response.data.image);
          }
          else {
            vm.$router.push({name: 'login'})
          }
        })
        .catch(function (error) {
          alert(error)
        });
      return
      }
      if(this.interface_==="2"){
      axios.post(this.host_business+'/business/get_business_info', formdata, {
        headers: {
          "content-type": "",
          "accept": ""
        }, withCredentials: false
      })
        .then(function (response) {
          if (response.data.status === "200") {
            [vm.new_src_images, vm.users_, vm.shoesinfos ] = get_catdetail(response.data.shoesinfo,
                                                                              response.data.user,
                                                                              response.data.image);
          }
          else {
            vm.$router.push({name: 'login'})
          }
        })
        .catch(function (error) {
          alert(error)
        });
      return
      }
      if(this.interface_==="3"){
      axios.post(this.host_business+'/business/get_business_info_tools', formdata, {
        headers: {
          "content-type": "",
          "accept": ""
        }, withCredentials: false
      })
        .then(function (response) {
          if (response.data.status === "200") {
            [vm.new_src_images_tools, vm.users_, vm.toolsinfos ] = get_catdetail(response.data.toolsinfo,
                                                                              response.data.user,
                                                                              response.data.image);
          }
          else {
            vm.$router.push({name: 'login'})
          }
        })
        .catch(function (error) {
          alert(error)
        });
      }

      },
    }
  }
</script>
