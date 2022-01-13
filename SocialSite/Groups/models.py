from django.db import models
from django.utils.text import slugify
import misaka
from django.contrib.auth import get_user_model
from django import template
from django.urls import reverse

#get current user
User = get_user_model()
#load custom templates
register = template.Library()

class Group(models.Model):
    """
    Group Model
    Attributes:
    Name: Character Field, unique has to be true because why have 2 groups with the same name
    Description: Text, description of the group's purpose
    Description_html: Uses Misaka module to allow html tags to do it's join in description
    Members: Many to many field with users that are considered Group Members
    """
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='Enter Default Text Here')
    description_html = models.TextField(editable=False,default='',blank=True)
    members = models.ManyToManyField(User,through='GroupMember')

    def __str__(self):
        return self.name
    
    #save slugified html link and description
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args,**kwargs)

    #get html url link using reverse on posts and the slugified html link
    def get_absolute_url(self):
        return reverse('Groups:single',kwargs={'slug':self.slug})

    #order
    class Meta:
        ordering = ['name']

class GroupMember(models.Model):
    """
    Group Member Model: Models to create relationships of users by groups
    Attributes:
    Group: Foreign key with Group model in Group App on related name of membership
    User: Foreign key with current User/ User=get_user_model
    """
    group = models.ForeignKey(Group, related_name='memberships', on_delete = models.CASCADE)
    user = models.ForeignKey(User,related_name='user_groups', on_delete = models.CASCADE)

    #return username if str representation if needed
    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group', 'user')


