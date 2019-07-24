from django.shortcuts import render
from django.http import HttpResponse
from cinemalog.Modules.news_crawler import crawler
# Create your views here.

def index(request):
    return HttpResponse('this is the index of cinemalog')

def crawlNews(request):
     return HttpResponse(crawler())
