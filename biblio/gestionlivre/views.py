from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import Book

from django.http import HttpResponse

# Create your views here.
def index(request):
    result = Book.objects.all()
    context={"listbooks":result}
    return render(request, 'myapp/index.html',context)
def fctBook(request,book_id):
    result = Book.objects.get(pk=book_id)
    context={"details":result}
    return render(request, 'myapp/detail.html',context)







