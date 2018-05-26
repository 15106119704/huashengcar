from django.shortcuts import render,redirect
from django.views.generic import View
from apps.production.models import Brande,Carstyle
from django.http import HttpResponse,JsonResponse
from django.conf import settings
import re,os
from apps.user.models import User, Address
from django.contrib.auth import authenticate,login,logout
from itsdangerous import TimedJSONWebSignatureSerializer as Tr
from itsdangerous import SignatureExpired as Sd
from django.core.mail import send_mail
from celery_task.tasks import send_active_email
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from utils.mixin import LoginRequired
from django_redis import get_redis_connection
from alipay import Alipay


class UpdateCollect(View):
    def post(self,request):
        # 判断用户是否登录
        user = request.user
        if not user.is_authenticated():
            return JsonResponse({'info':'您没有登录'})
        # 接收数据
        carid_after=request.POST.get('car_id')
        # 校验
        if not all([carid_after]):
            return JsonResponse({'info':'数据不完整'})
        try:
            caraf_2=int(carid_after)
        except Exception as e:
            return JsonResponse({'info':'数据错误'})
        try:
            Carstyle.objects.get(id=caraf_2)
        except Exception as e:
            return JsonResponse({'info':'您请求的数据不存在'})

        # 更新
        cn = get_redis_connection('default')
        key = 'col_%d' % user.id
        values = cn.lrange(key, 0, -1)

        if car.status == 0
            return JsonResponse({'info': '该车已售完'})
        return JsonResponse({'info': '更新成功'})
class Create(View):
    def post(self,request):
        # 判断登录
        request.user
        # 取数据
        # 判断数据是否合法
        # 插入数据到数据库

class ShowOrder(request):
    # return render(request,)
        pass

class Cost(View):
    def post(self,request):
        user = request.user
        if not user.is_authenticated():
            return redirect(reverse('user:login'))

        ordid_after = request.POST.get('order_id')
        if not ordid_after:
            return JsonResponse({'info':'订单不存在'})
        try:
            Order.objects.get(order_id=ordid_after,user=user,pay_style=1,states=0)
        except Exception as e:
            return JsonResponse({'indo':'订单不存在'})
        # alipay = Alipay(
        #     appid=''
        #     app_notify
        # )
        alipay = Alipay(
            appid='2016091400508206',
            app_notify_url=None,  # 默认回调url
            app_private_key_path=os.path.join(settings.BASE_DIR, "user/orderform/app_private_key.pem"),
            alipay_public_key_path=os.path.join(settings.BASE_DIR, "user/orderform/app_public_key.pem"),
        # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            sign_type="RSA2",  # RSA 或者 RSA2
            debug=True  # 默认False  配合沙箱模式使用
            )

        ord_cost = order.tprice
        order_sit=alipay.api_alipay_trade_page_pay(
            subject='hsrsc',
            out_trade_no=ordid_after,
            total_amount=ord_cost,
            return_url=None,
            notify_url=None,
        )
        # alipay.api_alipay_trade_page_pay这里应该有个结果返回接口
        url = 'https://openapi.alipaydev.com/gateway.do'+ordid_after
        return JsonResponse({'info':'','cost_url':url})


class Check(View):
    def post(self,request):



