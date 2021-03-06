from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import re
from apps.user.models import User, Address
from django.views.generic import View
from django.contrib.auth import authenticate,login,logout
from itsdangerous import TimedJSONWebSignatureSerializer as Tr
from itsdangerous import SignatureExpired as Sd
from django.core.mail import send_mail
from celery_task.tasks import send_active_email
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from utils.mixin import LoginRequired
# Create your views here.

# 127.0.0.1：8000/user/register
def register(request):
    if request.method == 'GET':
        # get
        return render(request, 'user/zhuce.html')
    elif request.method == 'POST':
        username = request.POST.get('user_name')
        phone = request.POST.get('phone')
        password = request.POST.get('possword')
        email = request.POST.get('email')
        allow = request.POST.get('allow')

        if not all([username, phone, password, email]):
            return render(request, 'user/zhuce.html', {'info': '数据不完整'})

        if not re.match(r'^1\d{10}$', phone):
            return render(request, 'user/zhuce.html', {'info': '手机号码错误'})

        if not re.match(r'^[a-z0-9A-Z]+@(qq|126|163)', email):
            return render(request, 'user/zhuce.html', {'info': '邮箱不正确'})
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None
        if User:
            return render(request, 'user/zhuce.html', {'info': '用户名已存在'})

        user = User.objects.create_user(username, phone, password, email)
        user.is_active = 0
        # 激活标志设置为0
        user.save()

        return render(request, 'user/登录/../../templates/user/denglu.html')


def register_handle(request):
    # 接受数据/数据校验/存储数据/
    username = request.POST.get('user_name')
    phone = request.POST.get('phone')
    password = request.POST.get('possword')
    email = request.POST.get('email')
    allow = request.POST.get('allow')

    if not all([username, phone, password, email]):
        return render(request, 'user/zhuce.html', {'info': '数据不完整'})

    if not re.match(r'^1\d{10}$', phone):
        return render(request, 'user/zhuce.html', {'info': '手机号码错误'})

    if not re.match(r'^[a-z0-9A-Z]+@(qq|126|163)', email):
        return render(request, 'user/zhuce.html', {'info': '邮箱不正确'})

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        user = None
    if User:
        return render(request, 'user/zhuce.html', {'info': '用户名已存在'})

    user = User.objects.create_user(username, phone, password, email)
    user.is_active = 0
    user.save()
    return render(request, 'user/登录/../../templates/user/denglu.html')


class Register(View):
    def get(self, request):
        return render(request, 'user/zhuce.html')

    def post(self, request):
        username = request.POST.get('user_name')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        email = request.POST.get('email')
        allow = request.POST.get('allow')
        # return HttpResponse([username,phone,password])
        if not all([username, phone, password]):
            return render(request, 'user/zhuce.html', {'info': '数据不完整'})

        if not re.match(r'^1(3|4|5|7|8)\d{9}$', phone):
            return render(request, 'user/zhuce.html', {'info': '手机号码错误'})

        if not re.match(r'^[a-z0-9A-Z]+@(qq|126|163)', email):
            return render(request, 'user/zhuce.html', {'info': '邮箱不正确'})
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None
        if user:
            return render(request, 'user/zhuce.html', {'info': '用户名已存在'})
        user = User.objects.create_user(username=username, password=password, email=email)
        # 激活标志设为0
        user.is_active = 0
        user.save()
        # 进行激活邮件的设置
        # /user/active/id(username,phone)/
        tr = Tr(settings.SECRET_KEY, 3600)
        dict_active = {'userid': user.id}
        active_info = tr.dumps(dict_active)
        # byte类型
        active_info = active_info.decode()
        # print(active_info)

        # 发送邮件
        send_active_email(user,active_info)

        return render(request, 'user/denglu.html')


class Active(View):
    def get(self, request, active_info):
        tr = Tr(settings.SECRET_KEY, 3600)
        try:
            info = tr.loads(active_info)
            userid = info['userid']
            user = User.objects.get(id=userid)
            user.is_active = 1
            user.save()
        except Sd:
            return HttpResponse('请重新获取激活链接')


class Login(View):
    def get(self, request):
        if 'username' in request.COOKIES:
            username = request.COOKIES.get('password')
        else:
            username = ''

        return render(request, 'user/denglu.html',{'username':username})

    def post(self, request):
        password = request.POST.get('password')
        username = request.POST.get('username')
        remember = request.POST.get('remember')

        if not all([username, password]):
            return render(request, 'user/denglu.html', {'info': '数据不完整'})

        user = authenticate(username=username, password=password)
        # 自带到登录验证

        if user is not None:
            if user.is_active:
                login(request,user)
                next_url = request.GET.get('next',reverse('user:login'))
                httpresponse = redirect(next_url)

                #记录登录状态login
                # httpresponse = HttpResponse('登录成功')
                httpresponse = redirect(reverse('user:register'))
                #redirect
                if remember == 'on':
                    httpresponse.set_cookie('password',password)
                else:
                    httpresponse.delete_cookie('password')
                return httpresponse

            else:
                return render(request, 'user/denglu.html', {'info': '您的账户未激活'})

        else:
            return render(request, 'user/denglu.html', {'info': '用户名或密码为空'})

class ProductionShow(View):
    def get(self,request):
        return render(request,'')

class Logout(LoginRequired,View):
    def get(self,request):
        logout(request=request)
        return redirect(reverse('production:index'))


class AddressView(View):
    def get(self,request):
        return render(request,'user/address.html')
    def post(self,request):
        address = request.POST.get('address')
        reciver = request.POST.get('reciver')
        post_num = request.POST.get('post_num')
        phone_num = request.POST.get('phone_num')
        if not all([address,reciver,post_num,phone_num]):
            return render(request,'user/address.html',{'info':'数据不完整'})
        if not re.match(r'^1(3|4|5|7|8)\d{9}$',phone_num):
            return render(request, 'user/address.html', {'info': '手机号不对'})

        user = request.user
        # try:
        #     address = Address.objects.get(user=user)
        # except Address.DoesNotExist:
        #     Address=None

        address_object = Address.objects.get_default_address(user=user)
        if address_object:
            is_default = False
        else:
            is_default = True

        Address.objects.create(user=user,reciver=reciver,post_num=post_num,phone_num=phone_num)

        return redirect(reverse('user:address'))





