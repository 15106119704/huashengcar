from django.shortcuts import render,redirect
from django.views.generic import View
from apps.production.models import Brande,Carstyle
from django.http import HttpResponse
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
from django.core.paginator import Paginator

# Create your views here.
# def index(request):
#     return render(request,'user/index.html')


class Index(View):
    def get(self,request):
        return render(request,'production/index.html')

class Detail(View):
    def get(self,request,p_id):
        try:
            car = Carstyle.objects.get(id=p_id)
        except Carstyle.DoesNotExist:
            return render(request, 'production/index.html')

        user = request.user
        if user.is_authenticated():
            cn = get_redis_connection('default')
            key = user.id
            val = car.id
            cn.lpush(key,val)
            cn.ltrim(key,0,19)
        else:
            return redirect(reversed('user:login'))


        context = {
            'carstyle':car
        }

class ShowAllCar(View):
    def get(self,request,b_id,page):
        try:
            brande_after = Brande.objects.get(id=b_id)
        except Brande.DoesNotExist:
            return redirect(reverse('production:index'))

        # 找到排序方式
        sort = request.GET.get('sort')
        if sort == 'default':
            car_list = Carstyle.objects.filter(brande=brande_after).order_by('id')

        elif sort == 'newest':
            car_list = Carstyle.objects.filter(brand=brande_after).order_by('create')
        elif sort == 'price':
            car_list = Carstyle.objects.filter(brand=brande_after).order_by('')
        elif sort == 'meter':
            car_list = Carstyle.objects.filter(brand=brande_after).order_by('')
        else:
            pass
        # 根据排序方式,获取数据
        # 进行分页
        paginator=Paginator(car_list,20)

        try:
            page_after = int(page)
        except Exception as e:
            page_after = 1

        numpage_after = paginator.num_pages
        # 分页所得的最大代码数
        # 总共展示7条数据

        if numpage_after<7:
            pages = range(1,numpage_after)
        else:
            if page_after<4:
                pages=range(1,8)
            elif numpage_after - page_after<3:
                pages = range(page_after-6,page_after+1)
            else:
                pages = range(page_after-3,page_after+4)



        context = {
            'page_after':page_after,
            'brande_after':brande_after,
            'car_list':car_list,
            'sort':sort,
        }
        return render(request,'production/list_show.html')

# class Search(View):
#     def get(self,request):
#         sql = 'select * from hs_carstyle where brande like 大众'
#
