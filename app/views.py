from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def app_uday(request):
    return HttpResponse('<h1><marquee><mark><i>i am uday</i></mark></marquee></h1>')