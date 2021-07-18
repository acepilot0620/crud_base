from account.models import Account
from os import error
from django.shortcuts import redirect, render,get_object_or_404

# Create your views here.

def main(request):
    if request.user.is_authenticated:
        now_user = request.user
        now_account = Account.objects.get(user=now_user)
        return render(request,'home.html',{"now_account":now_account})
    return render(request,'home.html')
