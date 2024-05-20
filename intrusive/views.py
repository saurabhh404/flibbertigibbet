from django.shortcuts import render

from intrusive.models import Post


def index(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(
        request,
        "intrusive/index.html",
        {
            "posts": posts,
        },
    )


def post_tags(request, tag):
    posts = Post.objects.filter(tags__name__contains=tag).order_by("-created_at")
    return render(
        request,
        "intrusive/tag.html",
        {
            "posts": posts,
            "tag": tag,
        },
    )


def detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(
        request,
        "intrusive/detail.html",
        {
            "post": post,
        },
    )
