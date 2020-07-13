from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'signup',views.signup,name='signup'),
    url(r'custreg', views.custreg, name='custreg'),
    url(r'login', views.login, name='login'),
    url(r'userhome', views.userhome, name='userhome'),
    url(r'validateuser', views.validateuser, name='validateuser'),

]