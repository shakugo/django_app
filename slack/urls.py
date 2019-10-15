from django.urls import path
from . import views

app_name = 'slack'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    path('login', views.Account_login.as_view(), name='login'),
]