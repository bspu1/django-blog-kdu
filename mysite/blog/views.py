from django.shortcuts import render
from .models import Post
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm


def post_list(request):
    # post_list = Post.published.all()
    # paginator = Paginator(post_list, 3)
    # page_number = request.GET.get("page", 1)
    # posts = paginator.page(page_number)
    # return render(request, "blog/post/list.html", {"posts": posts})
    post_list = Post.published.all()
    # Посторінкова розбивка з 3 постами на сторінку
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get("page", 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # Якщо page_number не ціле число, то
        # видати першу сторінку
        posts = paginator.page(1)
    except EmptyPage:
        # Якщо page_number знаходиться поза діапазоном, то
        # видати останню сторінку
        posts = paginator.page(paginator.num_pages)
    return render(request, "blog/post/list.html", {"posts": posts})


# def post_detail(request, id):
#     try:
#         post = Post.published.get(id=id)
#     except Post.DoesNotExist:
#         raise Http404("No Post found.")
#     return render(request, "blog/post/detail.html", {"post": post})


# def post_detail(request, id):
#     post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
#     return render(request, "blog/post/detail.html", {"post": post})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    comments = post.comments.all()
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect(request.path_info)
    else:
        comment_form = CommentForm()

    return render(
        request,
        "blog/post/detail.html",
        {"post": post, "comments": comments, "comment_form": comment_form},
    )
