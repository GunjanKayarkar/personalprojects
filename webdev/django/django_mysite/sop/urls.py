
from django.urls import path , include
from sop import views

urlpatterns = [
    
    path('',views.registra),
    path('login',views.loginhtml),
    path('detail',views.regdetail),
    path('Data',views.regdetailpa),

]