from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

from .forms import UserRegistrationForm, UserConfirmationForm

def signup(request):
    form = UserRegistrationForm()    
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("main:index")

    return render(request, 'signup.html', { 'form': form })

def signin(request):
    form = UserConfirmationForm()
    
    if request.method == 'POST':
        form = UserConfirmationForm(request, request.POST)

        if form.is_valid():
            login(request, form.get_user())
            return redirect("main:index")

    return render(request, 'signin.html', { 'form': form })


def signout(request):
    logout(request)
    
    return redirect('main:index')
