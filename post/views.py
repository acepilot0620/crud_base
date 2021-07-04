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
        return redirect('post_list')
    return render(request,'new_post.html')

def post_list(request):
    post_list = Post.objects.all()
    return render(request, 'post_list.html', {"post_list":post_list})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "post_detail.html", {"post":post})