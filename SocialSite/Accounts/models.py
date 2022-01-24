from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from PIL import Image

# Create your models here.
class EndUser(AbstractUser,PermissionsMixin):
    #username, email, password1,password2
    #return username with @ for social media "aesthetics"
    urls = models.URLField(blank=True,null=True)
    avatar = models.ImageField(default='default_profile.jpg', upload_to='media/profile_pics/')
    bio = models.TextField(blank=True,null=True)


    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        super(EndUser,self).save(*args,**kwargs)
        img = Image.open(self.avatar.path) # Open image
    # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) # Resize image
            img.save(self.avatar.path) # Save it again and override the larger image