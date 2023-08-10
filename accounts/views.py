from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from accounts import forms

# Create your views here.


def login_view(request):
    form = forms.LoginForm(request.POST or None)
    context = {
        'form': form
    }

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        print(username, password)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('posts:home_page')
        else:
            print('failed.')

    return render(request, 'accounts/login.html', context=context)


def logout_view(request):
    context = {}

    if request.method == 'POST':
        logout(request=request)
        return redirect('accounts:login')
    return render(request, 'accounts/logout.html', context=context)


def signup_view(request):
    form = forms.RegisterForm(request.POST or None)
    context = {
        'form': form
    }

    if form.is_valid():
        form.save()
        return redirect('accounts:login')

    return render(request, 'accounts/sign_up.html', context=context)