from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from . import forms
from django.contrib.auth.forms import UserChangeForm
# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserSignupForm
    #we use reverse lazy over here instead of lazy because we don't want to
    #execute before signing up
    template_name = 'Accounts/signup.html'
    success_url = reverse_lazy('login')

class EditUser(CreateView):
    #temporary form
    form_class = UserChangeForm
    template_name = 'Accounts/edit_profile.html'
    success_url = reverse_lazy('home')