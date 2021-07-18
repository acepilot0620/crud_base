from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Account
from django.contrib import messages

# Create your views here.

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        nickname = request.POST.get("nickname")
        if password1 != password2:
            messages.info(request,"비밀번호를 확인해주세요")
            return redirect("signup")
        else:
            new_user = User.objects.create_user(username = username,password = password1)
            new_user.save()
            new_account = Account(user=new_user, nickname=nickname)
            new_account.save()
            return redirect('login')
    return render(request,"signup.html")


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(request, username=username, password=password)
        print(user)
        if user is not None: # 회원 정보가 있을 때
            auth.login(request, user)
            return redirect('main')
        else:
            messages.info(request,"회원정보가 일치하지 않습니다.")
            return redirect("login")
    return render(request, "login.html")