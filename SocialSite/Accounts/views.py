from profile import Profile
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .forms import SignupForm, EditForm, ProfileUpdateForm
from django.contrib.auth import get_user_model

# Create your views here.
#
class SignUp(CreateView):
    model = get_user_model()
    form_class = SignupForm
    #we use reverse lazy over here instead of lazy because we don't want to
    #execute before signing up
    template_name = 'Accounts/signup.html'
    success_url = reverse_lazy('login')

class EditUser(UpdateView, LoginRequiredMixin):
    model = get_user_model()
    #temporary form
    form_class = EditForm
    template_name = 'Accounts/edit_user.html'
    success_url = reverse_lazy('Groups:all')


class UpdateProfile(UpdateView, LoginRequiredMixin):
    model = get_user_model()
    form_class = ProfileUpdateForm
    template_name = 'Accounts/edit_profile.html'
    success_url = reverse_lazy('profileview')

class ProfileView(DetailView):
    model = get_user_model()
    template_name = 'Accounts/profile_page.html'
    


