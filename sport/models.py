from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class ShoesInfo(models.Model):
    user = models.CharField(max_length=20, default="")
    shoesinfo = models.CharField(max_length=30, default="")
    shoesdetail = models.TextField(max_length=200, default="")
    price = models.IntegerField(default="")
    category = models.CharField(max_length=10, default="")
    image1 = models.FileField(upload_to='./font/static/media/shoes_image/%Y-%m-%d-%H-%M-%S', default="")
    image2 = models.FileField(upload_to='./font/static/media/shoes_image/%Y-%m-%d-%H-%M-%S', default="")
    image3 = models.FileField(upload_to='./font/static/media/shoes_image/%Y-%m-%d-%H-%M-%S', default="")

    class Meta:
        unique_together = (("user", "shoesinfo"),)

    def __str__(self):
        return self.shoesinfo


class ClothesInfo(models.Model):
    user = models.CharField(max_length=20, default="")
    clothesinfo = models.CharField(max_length=30, default="")
    clothesdetail = models.TextField(max_length=200, default="")
    price = models.IntegerField(default="")
    category = models.CharField(max_length=10, default="")
    image1 = models.FileField(upload_to='./font/static/media/clothes_image/%Y-%m-%d-%H-%M-%S', default="")
    image2 = models.FileField(upload_to='./font/static/media/clothes_image/%Y-%m-%d-%H-%M-%S', default="")
    image3 = models.FileField(upload_to='./font/static/media/clothes_image/%Y-%m-%d-%H-%M-%S', default="")

    class Meta:
        unique_together = (("user", "clothesinfo"),)

    def __str__(self):
        return self.clothesinfo


class ToolsInfo(models.Model):
    user = models.CharField(max_length=20, default="")
    toolsinfo = models.CharField(max_length=30, default="")
    toolsdetail = models.TextField(max_length=200, default="")
    price = models.IntegerField(default="")
    category = models.CharField(max_length=10, default="")
    image1 = models.FileField(upload_to='./font/static/media/tools_image/%Y-%m-%d-%H-%M-%S', default="")
    image2 = models.FileField(upload_to='./font/static/media/tools_image/%Y-%m-%d-%H-%M-%S', default="")
    image3 = models.FileField(upload_to='./font/static/media/tools_image/%Y-%m-%d-%H-%M-%S', default="")

    class Meta:
        unique_together = (("user", "toolsinfo"),)

    def __str__(self):
        return self.toolsinfo


class UserInfo(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    sex = models.CharField(max_length=20)
    old = models.IntegerField()
    mail = models.EmailField()
    interest = models.CharField(max_length=20)

    def __str__(self):
        return self.name
