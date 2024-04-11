from django.shortcuts import render
from django.http import HttpResponseNotFound

from .models import Post



def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.values()
    sorted_posts = [POSTS[key] for key in sorted(POSTS.keys(), reverse=True)]
    context = {'posts': sorted_posts}
    return render(request, template, context)


def post_detail(request, post_id: int):
    template = 'blog/detail.html'
    if post_id in POSTS:
        context = {'post': POSTS[post_id]}
        return render(request, template, context)
    return HttpResponseNotFound(f'Поста под id({post_id}) не существует!')


def category_posts(request, category_slug: str):
    template = 'blog/category.html'
    context = {'category_slug': category_slug}
    return render(request, template, context)
