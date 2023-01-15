from django.urls import path
from . import views
#path(url , function , name) you can execute this function if you get this url.
#url に対応するviews.py の関数を設定する
urlpatterns = [
    path('',views.index,name='index'),
]