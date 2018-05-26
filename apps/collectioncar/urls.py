from django.conf.urls import include, url
from apps.collectioncar.views import *

urlpatterns = [
    url(r'^addtion/$',AddtionCar.as_view(),name='addtion'),
    url(r'^search_car/$',search_car),
    url(r'^show/$',ShowCollect.as_view(),name='show'),
    url(r'^update/$',UpdateCollect.as_view,name='update'),
    url(r'^delete/$',DeleteCollect.as_view(),name='delete'),

]
