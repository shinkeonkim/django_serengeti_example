from django.shortcuts import render, redirect
from django.contrib.auth import login

from .forms import UserRegistrationForm

def signup(request):
    form = UserRegistrationForm()    
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("main:index")

    return render(request, 'signup.html', { 'form': form })

