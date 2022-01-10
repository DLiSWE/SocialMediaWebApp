from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.User)

# from Groups.models import Group, GroupMember
# from Posts.models import Post
# admin.site.register(models.Group)
# admin.site.register(models.GroupMember)
# admin.site.register(models.Post)