# coding=utf-8
import logging

import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse

from sport.models import ShoesInfo, ClothesInfo, ToolsInfo, UserInfo


def cors(request, response):
    if request.POST["from"] == "8080":
        response["Access-Control-Allow-Origin"] = "http://localhost:8080"
    if request.POST["from"] == "8081":
        response["Access-Control-Allow-Origin"] = "http://localhost:8081"
    response["Access-Control-Allow-Credentials"] = "true"
    response["Access-Control-Allow-Methods"] = "POST,GET,OPTIONS,DELETE"
    response["Access-Control-Allow-Headers"] = "origin, content-type, accept"
    return response


def login_in(request):
    if request.method == "POST":
        user = authenticate(username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            if user.is_active:
                login(request, user)
                try:
                    info = UserInfo.objects.get(user=User.objects.get(username=request.POST["username"]))
                    print(info)
                    response = HttpResponse(json.dumps({"status": "211", "info": "此用户已经录入资料"}))
                    return cors(request, response)
                except:
                    response = HttpResponse(json.dumps({"status": "200", "info": ""}))
                    return cors(request, response)
            else:
                response = HttpResponse(json.dumps({"status": "201", "error": "此账户已被禁用"}))
                return cors(request, response)
        else:
            response = HttpResponse(json.dumps({"status": "202", "error": "用户名或密码错误"}))
            return cors(request, response)
    else:
        if request.user.is_authenticated():
            response = HttpResponse(json.dumps({"status": "200", "info": ""}))
            return cors(request, response)
        else:
            response = HttpResponse(json.dumps({"status": "203", "error": "账户未登入"}))
            return cors(request, response)


def register_in(request):
    if request.method == "POST":
        if request.POST["username"]=="" or request.POST["password"] == "":
            response = HttpResponse(json.dumps({"status": "203", "error": "账户及密码不能为空"}))
            return cors(request, response)
        if int(len(request.POST["username"])) <= 20 and int(len(request.POST["password"])) <= 20:
            user = User.objects.create_user(username=request.POST["username"], password=request.POST["password"])
            user.save()
            response = HttpResponse(json.dumps({"status": "200", "error": "您已注册成功"}))
            return cors(request, response)
        else:
            response = HttpResponse(json.dumps({"status": "201", "error": "您输入的用户名及密码超过20位"}))
            return cors(request, response)
    else:
        response = HttpResponse(json.dumps({"status": "202", "error": "请输入需要注册的用户名及密码"}))
        return cors(request, response)


def loginout(request):
    logout(request)
    response = HttpResponse(json.dumps({"status": "200", "tip": "登出成功"}))
    return cors(request, response)


def get_shoes_info(request):
    print(len(request.FILES))
    if request.method == 'POST':
        try:
            ShoesInfo.objects.filter(user=request.POST['user']).get(shoesinfo=request.POST['shoesinfo'])
            response = HttpResponse(json.dumps({"status": "202", "tip": "商城已录入过此信息"}))
            return cors(request, response)
        except:
            if len(request.FILES) == 1:
                shoesinfo_new = ShoesInfo(shoesinfo=request.POST['shoesinfo'],
                                          shoesdetail=request.POST['shoesdetail'],
                                          price=request.POST['price'],
                                          image1=request.FILES['image1'],
                                          category=request.POST['category'],
                                          user=request.POST['user'])
                shoesinfo_new.save()
            elif len(request.FILES) == 2:
                shoesinfo_new = ShoesInfo(shoesinfo=request.POST['shoesinfo'],
                                          shoesdetail=request.POST['shoesdetail'],
                                          price=request.POST['price'],
                                          image1=request.FILES['image1'],
                                          image2=request.FILES['image2'],
                                          category=request.POST['category'],
                                          user=request.POST['user'])
                shoesinfo_new.save()
            else:
                shoesinfo_new = ShoesInfo(shoesinfo=request.POST['shoesinfo'],
                                          shoesdetail=request.POST['shoesdetail'],
                                          price=request.POST['price'],
                                          image1=request.FILES['image1'],
                                          image2=request.FILES['image2'],
                                          image3=request.FILES['image3'],
                                          category=request.POST['category'],
                                          user=request.POST['user'])
                shoesinfo_new.save()
            response = HttpResponse(json.dumps({"status": "200", "tip": "上传商城系统数据成功"}))
            return cors(request, response)

    else:
        json_data = dict()
        json_data["status"] = "202"
        json_data["tip"] = "请使用post请求"
        response = HttpResponse(json.dumps(json_data))
        return cors(request, response)


def get_clothes_info(request):
    print(len(request.FILES))
    if request.method == 'POST':
        try:
            ClothesInfo.objects.filter(user=request.POST['user']).get(clothesinfo=request.POST['clothesinfo'])
            response = HttpResponse(json.dumps({"status": "202", "tip": "商城已录入过此信息"}))
            return cors(request, response)
        except:
            if len(request.FILES) == 1:
                clothesinfo_new = ClothesInfo(clothesinfo=request.POST['clothesinfo'],
                                              clothesdetail=request.POST['clothesdetail'],
                                          price=request.POST['price'],
                                          image1=request.FILES['image1'],
                                          category=request.POST['category'],
                                          user=request.POST['user'])
                clothesinfo_new.save()
            elif len(request.FILES) == 2:
                clothesinfo_new = ClothesInfo(clothesinfo=request.POST['clothesinfo'],
                                              clothesdetail=request.POST['clothesdetail'],
                                          price=request.POST['price'],
                                          image1=request.FILES['image1'],
                                          image2=request.FILES['image2'],
                                          category=request.POST['category'],
                                          user=request.POST['user'])
                clothesinfo_new.save()
            else:
                clothesinfo_new = ClothesInfo(clothesinfo=request.POST['clothesinfo'],
                                              clothesdetail=request.POST['clothesdetail'],
                                          price=request.POST['price'],
                                          image1=request.FILES['image1'],
                                          image2=request.FILES['image2'],
                                          image3=request.FILES['image3'],
                                          category=request.POST['category'],
                                          user=request.POST['user'])
                clothesinfo_new.save()
            response = HttpResponse(json.dumps({"status": "200", "tip": "上传商城系统数据成功"}))
            return cors(request, response)

    else:
        json_data = dict()
        json_data["status"] = "202"
        json_data["tip"] = "请使用post请求"
        response = HttpResponse(json.dumps(json_data))
        return cors(request, response)


def get_tools_info(request):
    print(len(request.FILES))
    if request.method == 'POST':
        try:
            ToolsInfo.objects.filter(user=request.POST['user']).get(toolsinfo=request.POST['toolsinfo'])
            response = HttpResponse(json.dumps({"status": "202", "tip": "商城已录入过此信息"}))
            return cors(request, response)
        except:
            if len(request.FILES) == 1:
                toolsinfo_new = ToolsInfo(toolsinfo=request.POST['toolsinfo'],
                                          toolsdetail=request.POST['toolsdetail'],
                                          price=request.POST['price'],
                                          image1=request.FILES['image1'],
                                          category=request.POST['category'],
                                          user=request.POST['user'])
                toolsinfo_new.save()
            elif len(request.FILES) == 2:
                toolsinfo_new = ToolsInfo(toolsinfo=request.POST['toolsinfo'],
                                          toolsdetail=request.POST['toolsdetail'],
                                          price=request.POST['price'],
                                          image1=request.FILES['image1'],
                                          image2=request.FILES['image2'],
                                          category=request.POST['category'],
                                          user=request.POST['user'])
                toolsinfo_new.save()
            else:
                toolsinfo_new = ToolsInfo(toolsinfo=request.POST['toolsinfo'],
                                          toolsdetail=request.POST['toolsdetail'],
                                          price=request.POST['price'],
                                          image1=request.FILES['image1'],
                                          image2=request.FILES['image2'],
                                          image3=request.FILES['image3'],
                                          category=request.POST['category'],
                                          user=request.POST['user'])
                toolsinfo_new.save()
            response = HttpResponse(json.dumps({"status": "200", "tip": "上传商城系统数据成功"}))
            return cors(request, response)

    else:
        json_data = dict()
        json_data["status"] = "202"
        json_data["tip"] = "请使用post请求"
        response = HttpResponse(json.dumps(json_data))
        return cors(request, response)


def login_re(request):
    if request.method == "OPTIONS":
        response = HttpResponse(json.dumps({"status": "210", "info": ""}))
        return cors(request, response)
    if request.method == "POST":
        if request.user.is_authenticated:
            response = HttpResponse(json.dumps({"status": "200", "info": "处于登入状态", "username":request.user.username}))
            return cors(request, response)
        else:
            response = HttpResponse(json.dumps({"status": "202", "info": "请登入"}))
            return cors(request, response)
    else:
        response = HttpResponse(json.dumps({"status": "203", "info": "请使用psot请求"}))
        return cors(request, response)


def get_business_info(request):
    if request.method == "OPTIONS":
        response = HttpResponse(json.dumps({"status": "210", "shoesinfo": "none"}))
        return cors(request, response)
    if request.method == "POST":
        shoeinfo_ = ShoesInfo.objects.filter(category=request.POST["category"])
        list_shoesinfo = [i.shoesinfo for i in shoeinfo_]
        list_image = [i.image1 for i in shoeinfo_]
        list_users = [i.user for i in shoeinfo_]
        print(list_shoesinfo)
        print(list_image)
        response = HttpResponse(json.dumps({"status": "200", "shoesinfo": str(list_shoesinfo),
                                            "image": str(list_image), "user": str(list_users)}))
        return cors(request, response)
    else:
        response = HttpResponse(json.dumps({"status": "202", "shoesinfo": "none"}))
        return cors(request, response)


def get_business_info_clothes(request):
    if request.method == "OPTIONS":
        response = HttpResponse(json.dumps({"status": "210", "clothesinfo": "none"}))
        return cors(request, response)
    if request.method == "POST":
        clothesinfo_ = ClothesInfo.objects.filter(category=request.POST["category"])
        list_clothesinfo = [i.clothesinfo for i in clothesinfo_]
        list_image = [i.image1 for i in clothesinfo_]
        list_users = [i.user for i in clothesinfo_]
        print(list_clothesinfo)
        print(list_image)
        response = HttpResponse(json.dumps({"status": "200", "clothesinfo": str(list_clothesinfo),
                                            "image": str(list_image), "user": str(list_users)}))
        return cors(request, response)
    else:
        response = HttpResponse(json.dumps({"status": "202", "clothesinfo": "none"}))
        return cors(request, response)


def get_business_info_tools(request):
    if request.method == "OPTIONS":
        response = HttpResponse(json.dumps({"status": "210", "toolsinfo": "none"}))
        return cors(request, response)
    if request.method == "POST":
        toolsinfo_ = ToolsInfo.objects.filter(category=request.POST["category"])
        list_toolsinfo = [i.toolsinfo for i in toolsinfo_]
        list_image = [i.image1 for i in toolsinfo_]
        list_users = [i.user for i in toolsinfo_]
        print(list_toolsinfo)
        print(list_image)
        response = HttpResponse(json.dumps({"status": "200", "toolsinfo": str(list_toolsinfo),
                                            "image": str(list_image), "user": str(list_users)}))
        return cors(request, response)
    else:
        response = HttpResponse(json.dumps({"status": "202", "toolsinfo": "none"}))
        return cors(request, response)


def get_one_info(request):
    if request.method == "POST":
        shoeinfo = ShoesInfo.objects.filter(user=request.POST["user"]).get(shoesinfo=request.POST["shoesinfo"])
        print(shoeinfo.image1)
        response = HttpResponse(json.dumps({"status": "200", "price": str(shoeinfo.price), "image1":str(shoeinfo.image1),
                                            "image2": str(shoeinfo.image2),"image3":str(shoeinfo.image3), "shoesinfo":str(shoeinfo.shoesinfo), "shoesdetail":str(shoeinfo.shoesdetail)}))
        return cors(request, response)


def get_one_info_clothes(request):
    if request.method == "POST":
        clothesinfo = ClothesInfo.objects.filter(user=request.POST["user"]).get(clothesinfo=request.POST["clothesinfo"])
        print(clothesinfo.image1)
        print(clothesinfo.clothesdetail)
        response = HttpResponse(json.dumps({"status": "200", "price": str(clothesinfo.price), "image1":str(clothesinfo.image1),
                                            "image2": str(clothesinfo.image2),"image3":str(clothesinfo.image3), "clothesinfo":str(clothesinfo.clothesinfo), "clothesdetail":str(clothesinfo.clothesdetail)}))
        return cors(request, response)


def get_one_info_tools(request):
    if request.method == "POST":
        toolsinfo = ToolsInfo.objects.filter(user=request.POST["user"]).get(toolsinfo=request.POST["toolsinfo"])
        print(toolsinfo.image1)
        response = HttpResponse(json.dumps({"status": "200", "price": str(toolsinfo.price), "image1":str(toolsinfo.image1),
                                            "image2": str(toolsinfo.image2),"image3":str(toolsinfo.image3), "toolsinfo":str(toolsinfo.toolsinfo), "toolsdetail":str(toolsinfo.toolsdetail)}))
        return cors(request, response)


@login_required()
def save_user_info(request):
    if request.method == "POST":
        try:
            userinfo = UserInfo(user=User.objects.get(username=request.POST["username"]),
                                name=request.POST["name"],
                                phone=request.POST["phone"],
                                sex=request.POST["sex"],
                                old=request.POST["old"],
                                mail=request.POST["mail"],
                                interest=request.POST["interest"],)
            userinfo.save()
            response = HttpResponse(json.dumps({"status": "200", "info": "保存数据成功"}))
            return cors(request, response)
        except Exception as e:
            response = HttpResponse(json.dumps({"status": "202", "info": "请使用正确格式填写(年龄要求纯数字，邮箱格式要求正确)"}))
            # response = HttpResponse(json.dumps({"status": "202", "info": str(e)}))
            return cors(request, response)
    else:
        response = HttpResponse(json.dumps({"status": "203", "info": "请使用post请求"}))
        return cors(request, response)


def get_userinfo(request):
    if request.method == "POST":
        print(request.POST["user"])
        userinfo = UserInfo.objects.get(user=User.objects.get(username=request.POST["user"]))
        record_list = []
        record = {"name": userinfo.name,
                  "phone": userinfo.phone,
                  "sex": userinfo.sex,
                  "old": userinfo.old,
                  "mail": userinfo.mail,
                  "interest": userinfo.interest}
        record_list.append(record)
        response = HttpResponse(json.dumps({"status": "200", "info": str(record_list)}))
        return cors(request, response)
    else:
        response = HttpResponse(json.dumps({"status": "202", "info": "请使用post请求"}))
        return cors(request, response)