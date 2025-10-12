from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views
from .views import *
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', home, name='home'),
    path('main/', main, name='main'),
    path('about/', about, name='about'),
    path('index/', index, name='index'),
    path('order/', order, name='order'),
    path('order_form/', order_form, name='order_form'),
    #path('createorder/', createorder, name='createorder'),
    path('showmain/', showmain, name='showmain'),
    path('showmain2/', showmain2, name='showmain2'),
    path('createform/', createform, name='createform'),
    path('updateform/<int:id>/', updateform, name='updateform'),
    path('showmain3/', showmain3, name='showmain3'),
    path('showmain4/', showmain4, name='showmain4'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('deleteform/<int:id>/', deleteform, name='deleteform'),
    path('signup/', signup, name='signup'),
    path('login/', views.LoginView.as_view(template_name='menucard/registration/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view, name='logout'),
]
app_name = 'menucard'