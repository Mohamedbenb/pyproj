from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import Book
from .models import BlogPost
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

# TP7


class BlogView(ListView):
    model=BlogPost
    #=BlogPost.objects.all()
    context_object_name='posts'#posts à utiliser dans les pages html
    template_name="Posts/blogView.html"
class blogcreate(CreateView):
    model = BlogPost
    fields=['title','content','author','created_on']# soit fields soit form
 
    #form_class=blogform formulaire dans forms.py
    template_name = "Posts/blogcreate.html"
    success_url=reverse_lazy('Posts:listhtml')
class blogUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'author','content']
    pk_url_kwarg = 'pk'
    template_name = "Posts/blogUpdate.html"
    success_url=reverse_lazy('Posts:listhtml')
class blogDeleteView(DeleteView):
    model = BlogPost
    pk_url_kwarg = 'pk'
    template_name = "Posts/blogdelete.html"
    success_url=reverse_lazy('Posts:listhtml')



