from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from accounts.forms import LoginForm, UploadPublicationForm
from accounts.models import Publication, Publisher


def index(request):
    return HttpResponse("Hello, world")


def login_publisher_admin(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username, password = form.data['username'], form.data['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            # Redirect to a success page.
            return redirect('accounts/upload')
        else:
            return render(request, 'login.html', {'form': form, 'error': True})
            # Return an 'invalid login' error message.
    return render(request, 'login.html', {'form': form})


@login_required(redirect_field_name='/')
def upload_publication(request):
    if request.method == 'POST':
        form = UploadPublicationForm(request.POST, request.FILES)
        if form.is_valid():
            instance = Publication(
                publisher=request.user.publisher,
                title=form.cleaned_data.get('title'),
                pdf=request.FILES['pdf']
                )
            return HttpResponse('The file is saved')
    else:
        form = UploadPublicationForm()
        context = {
            'form':form,
        }
    return render(request, 'upload.html', context)