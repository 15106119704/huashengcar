from django.db import models

# Create your models here.
from db.base_model import BaseModel
from tinymce.models import HTMLField

# class Production(BaseModel):
#     user = models.ForeignKey('User',verbose_name='拥有者')
#     address = models.CharField(max_length=50,verbose_name='收货地址')
#     recieve = models.CharField(max_length=20,verbose_name='收件人')
#     phone_num = models.CharField(max_length=20,verbose_name='联系方式')
#     post_num = models.CharField(max_length=6,null=True,verbose_name='邮政编码')
#
# class Production(BaseModel):
#     zhuren = models.CharField(max_length=20,verbose_name='主人')
#     xinghao = models.CharField(max_length=20,verbose_name='型号')
#     price = models.CharField(max_length=10,verbose_name='价格')
#

class Brande(BaseModel):
    name = models.CharField(max_length=10,verbose_name='品牌')
    image = models.ImageField(upload_to='xxx',verbose_name='汽车品牌图片')
    introduce = HTMLField(blank=True,verbose_name='品牌介绍')

    class Meta:
        db_table = 'hs_brande'
        verbose_name = '汽车品牌'

    def __str__(self):
        return self.name

class Carstyle(BaseModel):
    status = models.IntegerField(choices=((0,'售完'),(1,'在售')))
    image = models.ImageField(upload_to='xxx',verbose_name='车辆真实状况')
    deteil = HTMLField(blank=True,verbose_name='车辆情况简介')
    color = models.CharField(max_length=5,verbose_name='颜色')
    price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='价格')
    mileage = models.IntegerField(verbose_name='里程数')
    brande = models.ForeignKey('Brande',verbose_name='品牌')
    # ower = models.ForeignKey('User',verbose_name='拥有者')

    class Meta:
        db_table = 'hs_carstyle'
        verbose_name = '车辆类型'