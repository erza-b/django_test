from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

from .models import Post


class PagesListView(ListView):
    model=Post
    template_name='home.html'

class PagesDetailView(DetailView):
    model=Post
    template_name='post_detail.html'

class PagesCreateView(CreateView):
    model=Post
    template_name='post_new.html'
    fields=['title','author','body']

class PagesUpdateView(UpdateView):
    model=Post
    template_name='post_edit.html'
    fields=['title','body']

