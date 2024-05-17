from django.shortcuts import render

from intrusive.models import Post
from intrusive.models import SideNote


def index(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "intrusive/index.html", {"posts": posts})


def detail(request, pk):
    post = Post.objects.get(pk=pk)
    side_notes = SideNote.objects.filter(post=post)
    return render(
        request,
        "intrusive/detail.html",
        {
            "post": post,
            "side_notes": side_notes,
        },
    )
