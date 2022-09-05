from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('vacancy:search_results')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('authentication:login')

    else:
        return render(request, 'authentication/login.html')


def home(request):
    return render(request, "authentication/home.html")

