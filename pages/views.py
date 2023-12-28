from django.views.generic import ListView,DetailView
from .models import Post


class PagesListView(ListView):
    model=Post
    template_name='home.html'

class PagesDetailView(DetailView):
    model=Post
    template_name='post_detail.html'