from celery import Celery
from django.conf import settings
from django.core.mail import send_mail



# 创建一个celery对象
app = Celery('celery_task.tasks',broker='redis://127.0.0.1:6379')

#初始化操作,创建任务函数
@app.task

# 创建任务
def send_active_email(user,active_info):
    subject = '花生二手车,优秀的二手车交易平台'
    message = ''
    from_email = settings.EMAIL_FROM
    reciver = [user.email]
    html_message = '<div>请点击您的激活链接</div><a href="http://127.0.0.1:8000/user/active/%s">gogogogogogo</a>' % active_info
    send_mail(subject, message, from_email, reciver, html_message=html_message)
    # subject = '花生二手车,优秀的二手车交易平台'
    # message = ''
    # from_email = settings.EMAIL_FROM
    # reciver = [user.email]
    # html_message = '<div>请点击您的激活链接</div><a href="http://127.0.0.1:8000/user/active/%s">gogogogogogo</a>' % active_info
    # send_mail(subject=subject, message=message, from_email=from_email, recipient_list=reciver, html_message=html_message)
