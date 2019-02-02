from django.conf.urls import url
from . import views
from django.urls import path, re_path

app_name = 'account'
urlpatterns = [
    path('login/', views.user_login, name='login'),
]