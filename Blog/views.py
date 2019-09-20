# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .form import CommentForm


from django.views import generic
from .models import *

def PostList(request):
    """list = Post.objects.filter(status=1).order_by('-date_created')
    template_name = "index.html"""

    list = Post.objects.filter(status=1).order_by('-date_created')
    context = {
        "list":list[0],
        "list2":list[1],
        "list3":list[2],
        "list4":list[3],
        "list5":list[4],
        "list6":list[5],
        "list7":list[6],
        "rest":list[3:],
    }
    return render(request, "post_list.html", context)


def PostDetail(request,pk):
    """model = Post
    template_name = 'post_detail.html'"""
    post = Post.objects.get(pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                content = form.cleaned_data["body"],
                post = post,
            )
            comment.save()
            return redirect("/blog/detail/" + str(post.pk))
    else:
        form = CommentForm()


    comments = Comment.objects.filter(post=post)
    context = {
        "post":post,
        "comments":comments,
        "form":form,

    }

    return render(request,"post_detail.html",context)

def PostCategory(request,category):
    posts = Post.objects.filter(category__name__contains=category)
    context = {
        "category":category,
        "posts":posts
    }

    return render(request, "post_category.html", context)

def PageNumber(request,page):
    page = int(page)
    try:
        display_posts = Post.objects.filter(status=1).order_by('-date_created')[(page * 7) - 8:]
    except IndexError:
        display_posts = None
        return render(request, "no_posts.html")
    if display_posts.count() > 7:
        display_posts = Post.objects.filter(status=1).order_by('-date_created')[(page * 7) - 5:(page*7)]

    context = {
        "posts": display_posts,
        "next":page+1,
    }

    return render(request, "post_list_continued.html",context)









