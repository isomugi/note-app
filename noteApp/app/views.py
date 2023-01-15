from django.shortcuts import render

# Create your views here.
#urls.py で紐づけられた関数が呼び出された時の挙動を決定する
#基本的にはhtmlを返す return render(request, 'ファイルの場所', context)
from django.http import HttpResponse

def index(request):
    return HttpResponse('hellow world')