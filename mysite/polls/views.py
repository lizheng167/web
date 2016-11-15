# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from polls.models import station

def index(request):
    start = request.GET.get('start')
    end   = request.GET.get('end')
    if start and end:
        stat  = station.objects.filter(start_station_name=start,end_station_name=end)
    else:
        stat  = station.objects.all()
    article_list = getPage(request, stat)
    return render(request, 'index.html', locals())


# 分页代码
def getPage(request, article_list):
    paginator = Paginator(article_list, 50)
    try:
        page = int(request.GET.get('page', 1))
        article_list = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        article_list = paginator.page(1)
    return article_list

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)