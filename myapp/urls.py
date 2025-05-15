from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),  
    path('login/', views.login, name='login'),  
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'), 
    path('buy/', views.buy, name='buy'), 
    path('rent/', views.rent, name='rent'),
    path('buy_house/', views.buy_house, name='buy_house'),
    path('buy_car/', views.buy_car, name='buy_car'), 
    path('profile/', views.profile, name='profile'),
]
