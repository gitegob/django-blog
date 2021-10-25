from django.shortcuts import render
from posts.models import Post

# Create your views here.


def index(request):
    posts = Post.objects.all()
    return render(request, 'blog_index.html', {'posts': posts})


def post(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'blog_post.html', {'post': post})
