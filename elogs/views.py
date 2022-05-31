from multiprocessing import context
from xml.etree.ElementTree import Comment
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from elogs.forms import PostForm,CommentForm
from django.http import HttpResponse
from .models import Author, Post,Comment
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer
import datetime

# Create your views here.


def index(request):
    # The Home Page Of Elog
    posts = Post.objects.order_by('date')
    context = {'posts': posts}
    return render(request,'elogs/index.html',context)


def posts(request):
    # Show All Posts
    posts = Post.objects.order_by('date')
    context = {'posts': posts}
    return render(request,'elogs/index.html',context)

@login_required
def new_post(request):
    # Add a new post
    if request.method != 'POST':
        # No data submitted, create a blank form
        form = PostForm()
    else:
        # Post data submitted, process data
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('elogs:posts')
    # Display a blank or invalid form
    context = {'form':form}
    return render(request,'elogs/new_post.html',context)


def comments(request,post_id):
    # Show a single post and all its comments
    post = Post.objects.get(id=post_id)
    comm = Comment.objects.filter(post=post_id)
    context = {'post':post,'comments':comm}
    return render(request,'elogs/comment.html',context)


@login_required
def add_comment(request,post_id):
    # Add a new comment to a particular post
    post = Post.objects.get(id=post_id)
    if request.method != 'POST':
        # No data submitted, create a blank form
        form = CommentForm()
    else:
        # POST data submitted, process data
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()
            return redirect('elogs:comments',post_id=post_id)
    context = {'post':post,'form':form}
    return render(request,'elogs/comment.html',context)


@login_required
def edit_comment(request,comment_id):
    # Edit an existing comment
    comment = Comment.objects.get(id=comment_id)
    post = comment.post
    if request.method != 'POST':
        # Initial request, pre-fill form with the current comment
        form = CommentForm(instance=comment)
    else:
        # Post data submitted, process data
        form = CommentForm(instance=comment, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('elogs:comments',post_id=post.id)
    context = {'comment':comment,'post':post,'form':form}
    return render(request,'elogs/edit_comment.html',context)


class PostList(APIView):
    #Get API data
    def get(self,request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)