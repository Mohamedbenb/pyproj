from .views import index,fctBook
from django.urls import path

urlpatterns = [
    path("",index,name='index'),
    path("<int:book_id>/",fctBook,name='htmlBook'),
]