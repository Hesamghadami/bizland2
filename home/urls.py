from django.urls import path
from .views import *

app_name = 'root'
urlpatterns =[
    path("",HomeListView.as_view(),name='home'),
]