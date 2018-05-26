from django.shortcuts import render,redirect
from django.views.generic import View
from apps.production.models import Brande,Carstyle
from django.http import HttpResponse,JsonResponse
from django.conf import settings
import re
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

class AddtionCar(View):
    def post(self,request):
        user = request.user
        if not user.is_authenticated():
            return redirect(reverse('user:login'))

        carid_after = request.POST.get('car_id')
        if not all([carid_after]):
            return JsonResponse({'info':'数据不完整操作'})
        try:
            car = Carstyle.objects.get(id=carid_after)
        except Carstyle.DoesNotExist:
            return JsonResponse({'info':'车辆不存在'})

        # 加入数据库
        cn = get_redis_connection('default')
        key = 'col_%d'%user.id
        cn.lpush(key,carid_after)
        return JsonResponse({'info':'加入收藏成功'})

def search_car(request):
    return render(request,'production/index.html')

class ShowCollect(View):
    def get(self,request):
        # 判断登录
        user=request.user
        if not user.is_authenticated():
            return redirect(reverse('user:login'))





    # 查询数据,在redis数据库里
    # 提取所需数据
    # 拼接上下文,分页
    # 返回结果


# ajax请求做更新操作
# 需要车辆的id
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

        # 构造上下文
        # 返回数据
        #



class DeleteCollect(View):
    def post(self,request):
        user = request.user
        if not user.is_authenticated():
            return JsonResponse({'info':'您没有登录'})
        carid_after=request.POST.get('car_id')
        if not all([carid_after]):
            return JsonResponse({'info':'数据不完整'})
        try:
            caraf_2=int(carid_after)
        except Exception as e:
            return JsonResponse({'info':'数据错误'})
        try:
            Carstyle.objects.get(id=caraf_2)
        except Exception as e:
            return JsonResponse({'info':'您请求到数据不存在'})

        cn = get_redis_connection('default')
        key = 'col_%d'%user.id
        cn.lrem(key,1,caraf_2)
        cn.llen(key)
        return JsonResponse({'info':'删除成功'})



