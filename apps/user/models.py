from django.db import models
from django.contrib.auth.models import AbstractUser
from db.base_model import BaseModel


# Create your models here.
class User(AbstractUser,BaseModel):
#用户模型到设计与实现
    class Meta:
        db_table='hs_user'
        verbose_name='用户'

class Address(BaseModel):
    user = models.ForeignKey('User',verbose_name='拥有者')
    address = models.CharField(max_length=50,verbose_name='收货地址')
    recieve = models.CharField(max_length=20,verbose_name='收件人')
    phone_num = models.CharField(max_length=20,verbose_name='联系方式')
    post_num = models.CharField(max_length=6,null=True,verbose_name='邮政编码')

    class Meta:
        db_table = 'hs_address'
        verbose_name='地址'
