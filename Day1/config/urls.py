"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse, Http404
from django.shortcuts import render

LG26_batters_list = [
    {'name': '홍창기', 'position': 'RF', 'avg_25': 0.287, 'hr_25': 1},
    {'name': '신민재', 'position': '2B', 'avg_25': 0.313, 'hr_25': 1},
    {'name': 'Austin', 'position': '1B', 'avg_25': 0.313, 'hr_25': 31},
    {'name': '문보경', 'position': '3B', 'avg_25': 0.276, 'hr_25': 24},
    {'name': '문성주', 'position': 'LF', 'avg_25': 0.305, 'hr_25': 3},
    {'name': '박동원', 'position': 'C', 'avg_25': 0.253, 'hr_25': 22},
    {'name': '오지환', 'position': 'SS', 'avg_25': 0.253, 'hr_25': 16},
    {'name': '이재원', 'position': 'DH', 'avg_25': None, 'hr_25': None},
    {'name': '박해민', 'position': 'CF', 'avg_25': 0.276, 'hr_25': 3},
]

def index(request):
    return HttpResponse('<h1>hello</h1>')


def book_list(request):
    book_text = ''

    for i in range(0,10):
        book_text += f'book {i}<br>'

    return HttpResponse(book_text)


def book(request, num):
    book_text = f'book {num}번 페이지입니다.'
    return HttpResponse(book_text)


def language(request, lang):
    return HttpResponse(f'<h1>{lang} 언어 페이지입니다.</h1>')


def python(request):
    return HttpResponse(f'<h1>여기는 python 페이지</h1>')


def batters(request):
    # batter_names = [
    #     f'<a href="/LG26batter/{index}/">{batter["name"]}</a><br>'
    #     for index, batter in enumerate(LG26_batters_list, start=1)
    # ]
    #
    # response_text = '<br>'.join(batter_names)
    #
    # return HttpResponse(response_text)
    return render(request, template_name = 'batters.html', context = {'LG26_batters_list': LG26_batters_list})


def batter_detail(request, index):
    real_index = index - 1
    if real_index < 0 or real_index >= len(LG26_batters_list):
        raise Http404

    batter = LG26_batters_list[real_index]

    # response_text = (f'<h3>{index}번 타자</h3>'
    #                  f'<h1>{batter["name"]}</h1>'
    #                  f'<h4>포지션: {batter["position"]}</h4>'
    #                  f'<p>25년 타율: {batter["avg_25"]}</p>'
    #                  f'<p>25년 홈런: {batter["hr_25"]} 개</p>'
    #                  )
    # return HttpResponse(response_text)
    return render(request, 'batter.html', context={'batter': batter, 'index': index})


def gugu(request, num):
    if num < 2 or num > 99:
        raise Http404
    response_text = f"<h1>{num}단</h1>"
    for i in range(1,10):
        response_text += f"{num} x {i} = {num * i}<br>"

    return HttpResponse(response_text)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('book_list/', book_list),
    path('book_list/<int:num>/', book),
    path('language/python/',python),
    path('language/<str:lang>/',language),
    path('LG26batter/',batters),
    path('LG26batter/<int:index>/', batter_detail),
    path('gugu/<int:num>/', gugu),
]
