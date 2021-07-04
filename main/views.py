from os import error
from django.shortcuts import redirect, render

# Create your views here.

def main(request):
    if request.method == "POST":
        text = request.POST.get('user_input')
        word_list = text.split(' ')
        word_num = len(word_list)
        return render(request,'home.html',{"word_num":word_num,"text":text})
    return render(request,'home.html')

def login(request):
    if request.method == "POST": # 사용자가 로그인 버튼을 눌렀을 때 
        username_DB = 'acepilot0620'
        password_DB = '1234'
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username_DB == username and password_DB == password:
            return redirect('main')
        elif password != password_DB:
            error_msg = "비밀번호 오류"
            return render(request, 'login.html', {"error_msg":error_msg})
        elif username != username_DB:
            error_msg = "아이디 오류"
            return render(request, 'login.html', {"error_msg":error_msg})
    return render(request,'login.html')

# def main(request):
#     if request.method == "POST":
#         text = request.POST.get('text_input')
#         word_list = text.split(' ')
#         word_num = len(word_list)
#         return render(request,'home.html',{"word_num":word_num, "text":text})
#     return render(request,'home.html')
    
# def login(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         uasername_DB = "acepilot0620"
#         password_DB = "1234"
#         if username == uasername_DB and password == password_DB:
#             return redirect('main')
#         else:
#             error_msg = "정보가 정확하지 않습니다."
#             return render(request,'login.html',{"error_msg":error_msg})
#     return render(request,'login.html')

# def word_count(request):
#     text = request.POST.get('text_input')
#     word_list = text.split(' ')
#     print(word_list)
#     return render(request,'home.html',{})