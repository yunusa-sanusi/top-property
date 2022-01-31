from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from .forms import SignUpForm
from .tokens import account_activation_token

User = get_user_model()


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            message = messages.success(
                request, ('You have logged in successfully'))
            return redirect('home')
    return render(request, 'accounts/login.html')


def signup_view(request):
    form = SignUpForm()

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            subject = f'Activate Your {current_site} account'
            message = render_to_string('accounts/account-activation.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user)
            })
            email = EmailMessage(
                f'{current_site} - Password Reset',
                message,
                settings.EMAIL_HOST_USER,
                [user.email]
            )
            email.fail_silently = False
            email.send()
            messages.success(
                request, ('Signup Successful, Please confirm your email to complete registration'))
            return redirect('accounts:login')

    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)


def signout(request):
    logout(request)
    return redirect('accounts:login')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('accounts:login')
    else:
        return HttpResponse('Email activation failed.')
