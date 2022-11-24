from django.urls import path
from app.views import *
app_name='anything'
urlpatterns=[
    path('app_uday/',app_uday,name='app_uday')
]