from django.urls import path
from . import views

app_name = 'slack'
urlpatterns = [
    path('', views.index, name='index'),
]