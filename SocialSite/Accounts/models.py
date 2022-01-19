from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User


# Create your models here.
class User(auth.models.User,auth.models.PermissionsMixin):

    #return username with @ for social media "aesthetics"
    def __str__(self):
        return "@{}".format(self.username)

