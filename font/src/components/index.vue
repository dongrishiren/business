<template>

  <div class="index">
    <auth></auth>
    <link href="../assets/css/bootstrap.min.css">
    <div class="container-fluid">
      <div class="row" style="margin-top: 5%">
        <div class="col-md-4 ">
          <div class="col-md-8 col-md-offset-4">
            <h3 style="color: lightyellow;margin-top: 10%">欢迎来到运动的世界...</h3>
          </div>
        </div>

        <div class="col-md-4">
          <div id="myCarousel" class="carousel slide" style="height: 100%;width: 100%;">
            <!-- 轮播（Carousel）指标 -->
            <ol class="carousel-indicators">
              <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
              <li data-target="#myCarousel" data-slide-to="1"></li>
              <li data-target="#myCarousel" data-slide-to="2"></li>
            </ol>
            <!-- 轮播（Carousel）项目 -->
            <div class="carousel-inner">
              <div class="item active ">
                <img src="../../static/web_media/shoes_one/1.jpg" style="height: 100%;width: 100%" alt="First slide">
              </div>
              <div class="item">
                <img src="../../static/web_media/shoes_one/2.jpg" style="height: 100%;width: 100%" alt="Second slide">
              </div>
              <div class="item">
                <img src="../../static/web_media/shoes_one/3.jpg" style="height: 100%;width: 100%" alt="Third slide">
              </div>
            </div>
            <!-- 轮播（Carousel）导航 -->
            <a class="carousel-control left" href="#myCarousel"
               data-slide="prev">&lsaquo;</a>
            <a class="carousel-control right" href="#myCarousel"
               data-slide="next">&rsaquo;</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      <div class="row " style="margin-top: auto">
        <div class="col-md-4">
          <h2 align="center">服饰</h2>
          <img src="../../static/web_media/clothes.jpg" style="width: 100%;">
          <router-link :to="{ name: 'category', params: { 'category': '服饰' }}" class="btn btn-success btn-lg"
                       style="width:40%;">
            了解更多
          </router-link>
        </div>
        <div class="col-md-4">
          <h2 align="center">鞋类</h2>
          <img src="../../static/web_media/shoes.jpg" style="width: 100%;">
          <router-link :to="{ name: 'category', params: { 'category': '鞋类' }}" class="btn btn-success btn-lg"
                       style="width:40%;">
            了解更多
          </router-link>
        </div>
        <div class="col-md-4">
          <h2 align="center">配件</h2>
          <img src="../../static/web_media/tools.jpg" style="width: 100%;">
          <router-link :to="{ name: 'category', params: { 'category': '配件' }}" class="btn btn-success btn-lg"
                       style="width:40%;">
            了解更多
          </router-link>
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
    name: 'login',
    data () {
      return {
        error: '',
        password: ''
      }
    },


    created: function () {
    },
    methods: {
    }
  }
</script>
