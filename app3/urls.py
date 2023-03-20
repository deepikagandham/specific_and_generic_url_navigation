from django.urls import path
from app3.views import *

app_name='app3'
urlpatterns=[
    path('sample3/',sample3,name='sample3')
]