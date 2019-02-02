from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        #if the form is valid procceed
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

            #if user does not exist
            if user is not None:
                #if user is valid log him in
                if user.is_active:
                    login(request, user)
                    return render(request, 'crm/home.html')
                else:
                    return HttpResponse('Account is disabled')
            else:
                return HttpResponse('Username or Password is invalid')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form':form})
