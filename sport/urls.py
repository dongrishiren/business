from django.conf.urls import url
from sport import views

urlpatterns = [
    url(r'^login_in$', views.login_in, name="login_in"),
    url(r'^register_in', views.register_in, name="register_in"),
    url(r'^loginout$', views.loginout, name="loginout"),
    url(r'^get_shoes_info$', views.get_shoes_info, name='get_shoes_info'),
    url(r'^get_clothes_info$', views.get_clothes_info, name='get_clothes_info'),
    url(r'^get_tools_info$', views.get_tools_info, name='get_tools_info'),
    url(r'^login_re$', views.login_re, name="login_re"),
    url(r'^get_business_info$', views.get_business_info, name="get_business_info"),
    url(r'^get_one_info$', views.get_one_info, name="get_one_info"),
    url(r'^get_business_info_clothes$', views.get_business_info_clothes, name="get_business_info_clothes"),
    url(r'^get_business_info_tools$', views.get_business_info_tools, name="get_business_info_tools"),
    url(r'^get_one_info_clothes$', views.get_one_info_clothes, name="get_one_info_clothes"),
    url(r'^get_one_info_tools$', views.get_one_info_tools, name="get_one_info_tools"),
    url(r'^save_user_info$', views.save_user_info, name="save_user_info"),
    url(r'^get_userinfo$', views.get_userinfo, name="get_userinfo"),

]