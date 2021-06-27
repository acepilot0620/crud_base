from django.shortcuts import render, redirect
from .models import Post
# Create your views here.

def new_post(request):
    if request.method == 'POST':
        user_title = request.POST.get('title')
        user_content = request.POST.get('content')
        post = Post()
        post.title = user_title
        post.content= user_content
        post.save()
        return render(request, 'post_list.html')
    return render(request,'new_post.html')