from django.conf.urls import url,include
from apps.production.views import Index,Detail,ShowAllCar

urlpatterns = [

   url(r'^$',Index.as_view(),name='index'),
   url(r'^detial/(?P<p_id>\d+)$',Detail.as_view(),name='detail'),
   url(r'^show/?P<b_id>(\d+)/(?P<page>\d+)',ShowAllCar.as_view(),name='show'),
   url(r'^collection/',include('collections'))


]