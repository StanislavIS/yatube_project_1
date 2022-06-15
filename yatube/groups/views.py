from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница постов')


def group_posts(request):
    return HttpResponse('Пост группы')


#