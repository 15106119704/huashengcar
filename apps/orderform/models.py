from django.db import models

# Create your models here.
from db.base_model import BaseModel


class Order(BaseModel):

    STATUS_CHOICE = (
        (0,'已下单'),(1,'已支付'),(2,'配送'),(3,'等待手续完成'),(4,'完成订单')
    )

    order_id = models.CharField(max_length=50,primary_key=True,verbose_name='订单')
    user = models.ForeignKey('user.User',verbose_name='买家')
    address = models.ForeignKey('user.Address',verbose_name='收货地址')
    paystyle = models.SmallIntegerField(choices=((0,'贷款'),(1,'支付宝'),(2,'网银')),default=1,verbose_name='支付方式')
    status = models.SmallIntegerField(choices=STATUS_CHOICE,verbose_name='订单状态')
    tprice = models.DecimalField(max_digits=20, decimal_places=5, verbose_name='总价')


    class Meta:
        db_table = 'hs_order'
        verbose_name = '订单详情'