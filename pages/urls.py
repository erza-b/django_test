from django.urls import path
from .views import PagesListView,PagesDetailView,PagesCreateView,PagesUpdateView,PagesDeleteView

urlpatterns = [
    path('post/<int:pk>/delete/',PagesDeleteView.as_view(),name='post_delete'),
    path('post/<int:pk>/edit/', PagesUpdateView.as_view(), name='post_edit'),
    path('post/new/',PagesCreateView.as_view(),name='post_new'),
    path('',PagesListView.as_view(), name='home'),
    path('post/<int:pk>/',PagesDetailView.as_view(), name='post_detail'),
    
]