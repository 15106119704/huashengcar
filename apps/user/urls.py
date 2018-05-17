from django.conf.urls import url
from . import views
from apps.user.views import Register,Active,Login

urlpatterns = [

    # url(r'^registers/$',views.register,name='registers'),
    # url(r'^register_handler$',views.register_handle)
    url(r'register',Register.as_view(),name='register'),
    url(r'login',Login.as_view(),name='login'),
    url(r'^active/(?P<active_info>.*)',Active.as_view(),name='active'),
]