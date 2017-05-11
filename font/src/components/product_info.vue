<template xmlns:v-bind="http://www.w3.org/1999/xhtml">
  <div class="shoesdetail">
    <auth></auth>
    <div class="container">

      <div class="row">
        <h1>{{ $route.params.back_user }}</h1>

        <div class="col-sm-12 col-md-12" v-for="src_image in src_images">
          <img v-bind:src=src_image alt="" style="width: 100%">
        </div>
        <div v-if="$route.params.num ==='1'">
        <h2 style="color: white">{{clothesinfo}}</h2>
        <h4 style="color: white">{{clothesdetail}}</h4>
        </div>
        <div v-if="$route.params.num ==='2'">
        <h2 style="color: white">{{shoesinfo}}</h2>
        <h4 style="color: white">{{shoesdetail}}</h4>
        </div>
        <div v-if="$route.params.num ==='3'">
        <h2 style="color: white">{{toolsinfo}}</h2>
        <h4 style="color: white">{{toolsdetail}}</h4>
        </div>
        <div class="col-md-2 col-xs-4 col-xs-offset-8 col-md-offset-10">
          <h4 style="color: black"> 价格：{{ price }}元</h4>
          <router-link to="/buy" class="btn btn-danger btn-lg ">购买</router-link>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
  import axios from "axios";
  import "babel-polyfill";
    import auth from "./authentication.vue"
  export default {
    components: {"auth":auth},
    name: 'shoesdetail',
    data () {
      return {
          seen_login:"",
        seen_logout:"",
        shoesdetail: "",
        shoesinfo: "",
        clothesdetail: "",
        clothesinfo: "",
        toolsdetail: "",
        toolsinfo: "",
        price: "",
        src_image1: "",
        src_image2: "",
        src_image3: "",
        src_images:"",
      }
    },
    created: function () {
      const vm = this;
      document.title = "运动世界商城";

      formdata.append("user", this.$route.params.back_user);
      if (this.$route.params.num ==='2'){
                formdata.append("shoesinfo", this.$route.params.info);
      axios.post(this.host_business+'/business/get_one_info', formdata, {
        headers: {"content-type": "", "accept": ""},
        withCredentials: false
      })
        .then(function (response) {
          if (response.data.status === "200") {
            vm.price = response.data.price;
            vm.shoesinfo = response.data.shoesinfo;
            vm.shoesdetail = response.data.shoesdetail;
            vm.src_image1 = response.data.image1;
            vm.src_image1 = "/"+vm.src_image1.split("font/")[1];
            vm.src_image2 = response.data.image2;
            vm.src_image2 = "/" + vm.src_image2.split("font/")[1];
            vm.src_image3 = response.data.image3;
            vm.src_image3 = "/" + vm.src_image3.split("font/")[1];
            vm.src_images = [vm.src_image1,vm.src_image2,vm.src_image3,]
          }
          else {
            vm.$router.push({name: 'login'})
          }
        })
        .catch(function (error) {
          alert(error)
        })
      }
      if (this.$route.params.num ==='1'){
        formdata.append("clothesinfo", this.$route.params.info);
      axios.post(this.host_business+'/business/get_one_info_clothes', formdata, {
        headers: {"content-type": "", "accept": ""},
        withCredentials: false
      })
        .then(function (response) {
          if (response.data.status === "200") {
            vm.price = response.data.price;
            vm.clothesinfo = response.data.clothesinfo;
            vm.clothesdetail = response.data.clothesdetail;
            vm.src_image1 = response.data.image1;
            vm.src_image1 = "/" + vm.src_image1.split("font/")[1];
            vm.src_image2 = response.data.image2;
            vm.src_image2 = "/" + vm.src_image2.split("font/")[1];
            vm.src_image3 = response.data.image3;
            vm.src_image3 = "/" + vm.src_image3.split("font/")[1];
            vm.src_images = [vm.src_image1,vm.src_image2,vm.src_image3]
          }
          else {
            vm.$router.push({name: 'login'})
          }
        })
        .catch(function (error) {
          alert(error)
        })
      }
      if (this.$route.params.num ==='3'){
                formdata.append("toolsinfo", this.$route.params.info);
      axios.post(this.host_business+'/business/get_one_info_tools', formdata, {
        headers: {"content-type": "", "accept": ""},
        withCredentials: false
      })
        .then(function (response) {
          if (response.data.status === "200") {
            vm.price = response.data.price;
            vm.toolsinfo = response.data.toolsinfo;
            vm.toolsdetail = response.data.toolsdetail;
            vm.src_image1 = response.data.image1;
            vm.src_image1 = "/" + vm.src_image1.split("font/")[1];
            vm.src_image2 = response.data.image2;
            vm.src_image2 = "/" + vm.src_image2.split("font/")[1];
            vm.src_image3 = response.data.image3;
            vm.src_image3 = "/" + vm.src_image3.split("font/")[1];
            vm.src_images = [vm.src_image1,vm.src_image2,vm.src_image3]
          }
          else {
            vm.$router.push({name: 'login'})
          }
        })
        .catch(function (error) {
          alert(error)
        })
      }

    },
    methods: {
    },
  }

</script>
