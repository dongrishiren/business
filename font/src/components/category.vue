<template xmlns:v-on="http://www.w3.org/1999/xhtml">
  <div class="shoes">
    <auth></auth>
    <link href="../assets/css/bootstrap.min.css">
    <div class="container" >

      <!-----------------------------大标题提示栏----------------------------------------->
      <div class="jumbotron" style="background: orange">
        <div class="row">
          <div class="col-md-4">
            <button class="btn btn-lg btn-block btn-success" style="margin-top: 20%" v-on:click="change_title1">{{tab1}}</button>
          </div>
          <div class="col-md-4">
            <div v-if="shoe_ca">
        <h1>鞋类</h1>
        <h5>没有比脚更长的路，选双好鞋去远行！</h5>
            </div>
            <div v-if="clothes_ca">
              <h1>服饰</h1>
              <h5>运动的汗水是我们对梦想的追求！</h5>
            </div>
            <div v-if="tools_ca">
              <h1>配件</h1>
              <h5>兄弟，来场篮球怎样！</h5>
            </div>
          </div>
          <div class="col-md-4">
            <button class="btn btn-lg btn-block btn-info" style="margin-top: 20%" v-on:click="change_title2">{{tab2}}</button>
          </div>
      </div>
      </div>

<!---------------------------------------------循环显示类别----------------------------------------------->
<div v-if="shoe_ca">
      <div class="container">
        <div class="row " style="margin-top: auto">
          <div class="col-md-4" v-for="(category_shoes, index) in categorys_shoes">
            <h2 align="center">{{category_shoes}}</h2>
            <img v-bind:src=shoes_list[index] style="width: 100%;">
            <router-link :to="{name:'category_detail',params:{'category':category_shoes}}" class="btn btn-primary btn-lg" style="width:40%;" role="button">
              了解更多</router-link>
          </div>
        </div>
        </div>
      </div>


      <div v-if="clothes_ca">
        <div class="container">
          <div class="row " style="margin-top: auto">
            <div class="col-md-4" v-for="(category_clothes, index) in categorys_clothes">
            <h2 align="center">{{category_clothes}}</h2>
            <img v-bind:src=clothes_list[index] style="width: 100%;">
            <router-link :to="{name:'category_detail',params:{'category':category_clothes}}" class="btn btn-primary btn-lg" style="width:40%;" role="button">
              了解更多</router-link>
          </div>
          </div>
        </div>
      </div>


      <div v-if="tools_ca">
        <div class="container">
          <div class="row " style="margin-top: auto">
            <div class="col-md-4" v-for="(category_tools, index) in categorys_tools">
            <h2 align="center">{{category_tools}}</h2>
            <img v-bind:src=tools_list[index] style="width: 100%;">
            <router-link :to="{name:'category_detail',params:{'category':category_tools}}" class="btn btn-primary btn-lg" style="width:40%;" role="button">
              了解更多</router-link>
          </div>
          </div>
        </div>
      </div>



    </div>
    <p style="margin-top: 5%">     </p>
  </div>

</template>

<script>
  import axios from "axios";
  import "babel-polyfill";
    import auth from "./authentication.vue"
  export default {
    components: {"auth":auth},
    name: 'shoes',
    data () {
      return {
        categorys_shoes:["板鞋","篮球鞋","跑鞋","网鞋","帆布鞋","羽毛球鞋","足球鞋","拖鞋","凉鞋",],
        categorys_clothes:["夏季男装","夏季女装","冬季男装","冬季女装",],
        categorys_tools:["球类配件","袜子","箱包","手脚护腕","眼镜"],
        shoes_list:["../../static/web_media/shoes_category/banxie.jpg","../../static/web_media/shoes_category/lanqiuxie.jpg",
        "../../static/web_media/shoes_category/paoxie.jpg","../../static/web_media/shoes_category/wangxie.jpg",
        "../../static/web_media/shoes_category/fanbu.jpg","../../static/web_media/shoes_category/yumaoqiuxie.jpg",
        "../../static/web_media/shoes_category/zuqiuxie.jpg","../../static/web_media/shoes_category/tuoxie.jpg",
        "../../static/web_media/shoes_category/liangxie.jpg",],
        clothes_list:["../../static/web_media/clothes_category/xiajinanzhuang.jpg","../../static/web_media/clothes_category/xiajinvzhuang.jpg",
        "../../static/web_media/clothes_category/dongjinanzhuang.jpg","../../static/web_media/clothes_category/dongjinvzhuang.jpg",],
        tools_list:["../../static/web_media/tools_category/qiuleipeijian.jpg","../../static/web_media/tools_category/wazi.jpg",
        "../../static/web_media/tools_category/xiangbao.jpeg","../../static/web_media/tools_category/huwan.jpg",
        "../../static/web_media/tools_category/yanjing.jpg",],
        tab1:"服饰",
        tab2:"配件",
        shoe_ca:true,
        clothes_ca:"",
        tools_ca:"",
        seen_login:"",
        seen_logout:"",
        error: '',
        password: ''
      }
    },
    created: function () {
      const vm = this;
      document.title = "运动世界商城";

      if(this.$route.params.category==="服饰"){
        this.tab1 = "鞋类";
        this.tab2 = "配件";
        this.shoe_ca="";
        this.clothes_ca=true;
        this.tools_ca="";
      }
      if(this.$route.params.category==="配件"){
        this.tab1 = "鞋类";
        this.tab2 = "服饰";
        this.shoe_ca="";
        this.clothes_ca="";
        this.tools_ca=true;
      }

    },
    methods: {
      change_title1:function () {
        if(this.shoe_ca){
            if (this.tab1==="服饰"){
              this.tab1 = "鞋类";
              this.shoe_ca="";
              this.clothes_ca=true;
              this.tools_ca="";
              return
            }
            else {
              this.tab1 = "鞋类";
              this.shoe_ca="";
              this.clothes_ca="";
              this.tools_ca=true;
              return
            }

        }
        if(this.clothes_ca){
          if (this.tab1==="鞋类"){
            this.tab1 = "服饰";
            this.shoe_ca=true;
            this.clothes_ca="";
            this.tools_ca="";
            return
          }
          else{
            this.tab1 = "服饰";
            this.shoe_ca="";
            this.clothes_ca="";
            this.tools_ca=true;
            return
          }
        }
        if(this.tools_ca){
          if (this.tab1==="服饰"){
            this.tab1 = "配件";
            this.shoe_ca="";
            this.clothes_ca=true;
            this.tools_ca="";
          }
          else {
            this.tab1 = "配件";
            this.shoe_ca=true;
            this.clothes_ca="";
            this.tools_ca="";
          }
        }
      },
      change_title2:function () {
        if(this.shoe_ca){
          if (this.tab2==="服饰"){
            this.tab2 = "鞋类";
            this.shoe_ca="";
            this.clothes_ca=true;
            this.tools_ca="";
            return
          }
          else {
            this.tab2 = "鞋类";
            this.shoe_ca="";
            this.clothes_ca="";
            this.tools_ca=true;
            return
          }

        }
        if(this.clothes_ca){
          if (this.tab2==="鞋类"){
            this.tab2 = "服饰";
            this.shoe_ca=true;
            this.clothes_ca="";
            this.tools_ca="";
            return
          }
          else {
            this.tab2 = "服饰";
            this.shoe_ca="";
            this.clothes_ca="";
            this.tools_ca=true;
            return
          }
        }
        if(this.tools_ca){
          if (this.tab2==="服饰"){
            this.tab2 = "配件";
            this.shoe_ca="";
            this.clothes_ca=true;
            this.tools_ca="";
          }
          else {
            this.tab2 = "配件";
            this.shoe_ca=true;
            this.clothes_ca="";
            this.tools_ca="";
          }
        }
      },
    }
  }
</script>
