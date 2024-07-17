from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("안녕하세요 pydo에 오신것을 환영합니다.")
def index2(request):
    return HttpResponse("질문 목록")
def index3(request):
    return HttpResponse("안녕하세요 hello에 오신것을 환영합니다.")
def index4(request):
    return HttpResponse("안녕하세요 hello/1에 오신것을 환영합니다.")