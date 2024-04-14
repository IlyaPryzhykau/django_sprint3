from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Post, Category


MAX_POSTS = 5
POST_LIST = Post.objects.filter(
    is_published=True,
    category__is_published=True
)


def index(request):
    template = 'blog/index.html'
    post_list = POST_LIST.filter(
        pub_date__lte=timezone.now(),
    )

    context = {'post_list': post_list[:MAX_POSTS]}
    return render(request, template, context)


def post_detail(request, post_id: int):
    template = 'blog/detail.html'

    post = get_object_or_404(
        POST_LIST.filter(pub_date__lte=timezone.now()),
        pk=post_id
    )

    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug: str):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category, slug=category_slug, is_published=True)
    post_list = POST_LIST.filter(
        category=category,
        pub_date__lte=timezone.now()
    )
    context = {
        'category': category,
        'post_list': post_list
    }
    return render(request, template, context)
