from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from accounts.forms import LoginForm


def index(request):
    return HttpResponse("Hello, world")


def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username, password = form.data['username'], form.data['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            # Redirect to a success page.
            return redirect('/')
        else:
            return render(request, 'login.html', {'form': form, 'error': True})
            # Return an 'invalid login' error message.
    return render(request, 'login.html', {'form': form})