from django.urls import re_path, path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'Accounts'

urlpatterns = [
    re_path(r'^login/$', auth_views.LoginView.as_view(template_name='Accounts/login.html'),name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    re_path(r'^signup/$', views.SignUp.as_view(), name='signup'),
    re_path(r'^edit_profile/$', views.EditUser.as_view(), name='editprof'),
]