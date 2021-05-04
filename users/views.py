from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from .models import ProfileModel
from django.contrib.auth import user


def Register(request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account Has Been Created!You Are Able To Login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request ,'users/Register.html',{'form':form})

@login_required
def Profile(request):
    print(user.username)
    return render(request,'users/profile.html')


    