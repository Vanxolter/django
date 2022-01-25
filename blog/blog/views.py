from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, HttpResponse
import logging
from blog.forms import RegisterForm, Authorization
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            logger.info(form.cleaned_data)
            user = User(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect("/main")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})


def authorization(request):
    if '_signin' in request.POST:
        form = Authorization(request.POST)
        if form.is_valid():
            logger.info(form.cleaned_data)
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("/main")
            else:
                return HttpResponse('Аккаунта не существует')
    elif '_reg' in request.POST:
        return redirect("/register/")
    else:
        form = Authorization()
        return render(request, "authorization.html", {"form": form})