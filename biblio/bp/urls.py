from django.urls import path
from bp.views import BlogView,blogcreate,blogUpdateView,blogDeleteView

app_name="bp"
urlpatterns = [
path('liste',BlogView.as_view(),name='listhtml'),
path('create',blogcreate.as_view(),name='createhtml'),
path('update/<int:pk>',blogUpdateView.as_view(),name='updatehtml'),
path('delete/<int:pk>',blogDeleteView.as_view(),name='deletehtml'),]