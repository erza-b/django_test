from django.urls import path
from .views import PagesListView,PagesDetailView,PagesCreateView

urlpatterns = [
    path('post/new/',PagesCreateView.as_view(),name='post_new'),
    path('',PagesListView.as_view(), name='home'),
    path('post/<int:pk>/',PagesDetailView.as_view(), name='post_detail'),
    
]