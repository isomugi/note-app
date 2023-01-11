from django.urls import path
from . import views
#path(url , function , name) you can execute this function if you get this url.
urlpatterns = [
    path('',views.index,name='index'),
]