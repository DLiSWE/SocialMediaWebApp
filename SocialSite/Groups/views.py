from django.shortcuts import render
from django.contrib.auth.mixins import (LoginRequiredMixin, PermissionRequiredMixin)
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.shortcuts import get_object_or_404
from Groups.models import Group, GroupMember
from Posts.models import Post
from braces.views import SelectRelatedMixin
from . import models

class CreateGroup(LoginRequiredMixin,generic.CreateView):
    fields = ('name','description')
    model = Group

class SingleGroup(generic.DetailView):
    model = Group

class ListGroups(generic.ListView):
    model = Group

class JoinGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self,*args,**kwargs):
        return reverse('Groups:single', kwargs={'slug':self.kwargs.get('slug')})

#create query to assign user to group/one to many relationship
    def get(self,request,*args,**kwargs):
        group = get_object_or_404(Group, slug=self.kwargs.get('slug'))

        try:
            GroupMember.objects.create(user=self.request.user,group=group)
        #specify if groupmember is already in group
        except:
            messages.warning(self.request,'Already a member!')
        else:
            messages.success(self.request,'You are now a member!')

        return super().get(request,*args,**kwargs)

class LeaveGroup(LoginRequiredMixin,generic.RedirectView):

    def get_redirect_url(self,*args,**kwargs):
        return reverse('Groups:single', kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):
        
        try:
            membership = models.GroupMember.objects.filter(
                user=self.request.user,
                group__slug=self.kwargs.get('slug')).get()
        except models.GroupMember.DoesNotExist:
            messages.warning(self.request,'Whoops, you are not a member')
        else:
            membership.delete()
            messages.success(self.request,'You have left the group!')
        
        return super().get(request,*args,**kwargs)