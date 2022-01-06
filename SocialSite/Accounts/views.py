from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from . import forms
# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserSignupForm
    success_url = reverse_lazy('login')
    #we use reverse lazy over here instead of lazy because we don't want to
    #execute before signing up
    template_name = 'Accounts/signup.html'