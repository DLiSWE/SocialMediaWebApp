from django.urls import re_path, path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'Accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='Accounts/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('edit_profile/<int:pk>', views.EditUser.as_view(), name='editprof'),
]