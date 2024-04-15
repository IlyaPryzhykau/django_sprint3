from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Post, Category


MAX_POSTS = 5


def get_published_posts(category=None):
    queryset = Post.objects.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
    )
    if category:
        queryset = queryset.filter(category=category)
    else:
        queryset = queryset.filter(category__is_published=True)
    return queryset


def index(request):
    template = 'blog/index.html'
    post_list = get_published_posts()
    context = {
        'post_list': post_list[:MAX_POSTS]
    }
    return render(request, template, context)


def post_detail(request, post_id: int):
    template = 'blog/detail.html'
    post = get_object_or_404(
        get_published_posts(),
        pk=post_id
    )
    context = {
        'post': post
    }
    return render(request, template, context)


def category_posts(request, category_slug: str):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = get_published_posts(
        category=category
    )
    context = {
        'category': category,
        'post_list': post_list
    }
    return render(request, template, context)
