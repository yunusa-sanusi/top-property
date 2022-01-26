from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import SignUpForm
from agents.models import Agent


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
    return render(request, 'accounts/login.html')


def signup_view(request):
    form = SignUpForm()
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                agent = Agent.objects.get(user=user)
                return redirect('agents:agent-edit', agent.slug)

    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)


def signout(request):
    logout(request)
    return redirect('accounts:login')
