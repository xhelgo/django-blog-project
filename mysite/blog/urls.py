from django.urls import path

from blog.views import (
    PostListView,
    PostDetailView
    )

app_name = 'blog'

urlpatterns = [
    # post views
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail')
]
