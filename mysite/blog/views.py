from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView

from blog.models import Post

# Create your views here.


class PostListView(ListView):
    template_name = 'blog/post/post_list.html'

    def get_queryset(self):
        return Post.published.all()


class PostDetailView(DetailView):
    queryset = Post.published.all()
    template_name = 'blog/post/post_detail.html'
