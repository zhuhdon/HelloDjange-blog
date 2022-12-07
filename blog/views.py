from django.shortcuts import render, get_object_or_404
import markdown

from .models import Post


def index(request):
    post_list = Post.objects.all().order_by('-created')
    return render(request, 'blog/index.html', context={'post_list': post_list})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.fenced_code',
        'markdown.extensions.toc',
    ])
    return render(request, 'blog/detail.html', context={'post': post})
