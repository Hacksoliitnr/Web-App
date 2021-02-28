from django.shortcuts import render
from django.contrib.auth.views import (
    LoginView, 
    LogoutView
)
# Create your views here.

class Login(LoginView):
    template_name = 'authen/login.html'
    redirect_authenticated_user = True

class Logout(LogoutView):
    pass
    template_name = 'authen/logout.html'