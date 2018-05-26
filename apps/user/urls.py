from django.conf.urls import url
from apps.user.views import Register,Active,Login,ProductionShow,Logout,Address
from django.contrib.auth.decorators import login_required

urlpatterns = [

    # url(r'^registers/$',views.register,name='registers'),
    # url(r'^register_handler$',views.register_handle)
    url(r'register/',Register.as_view(),name='register'),
    url(r'login/',Login.as_view(),name='login'),
    url(r'^active/(?P<active_info>.*)',Active.as_view(),name='active'),
    url(r'production/',login_required(ProductionShow.as_view()),name='production'),
    url(r'logout/',Logout.as_view(),name='logout'),
    url(r'address/', Address.as_view(), name='address')

]