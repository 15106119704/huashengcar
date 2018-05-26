from django.conf.urls import include, url
from apps.orderform.views import *

urlpatterns = [
    url(r'^create/$', Create.as_view(), name='create'),
    url(r'^cost',Cost.as_view(),name='cost')
    url(r'^check', Check.as_view(), name='check')

]
