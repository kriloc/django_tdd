from django.urls import path, re_path
from . import views

app_name = 'lists'

urlpatterns = [
    re_path(r"^hello?/$", views.index),
    path('', views.home_page, name='home')

]