from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context={"mysite":"glsi3"}
    return render(request, 'index.html', context)