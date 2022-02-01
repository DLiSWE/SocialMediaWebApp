from django.db.models import query
from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import Http404, HttpResponseRedirect
from django.views import generic
from django.contrib.auth import get_user_model
from braces.views import SelectRelatedMixin
from django.contrib import messages
from . import models
from .form_post import CommentForm



# Create your views here.
User = get_user_model()

class PostList(SelectRelatedMixin, generic.ListView):
    model = models.Post
    select_related = ('user', 'group')

class UserPosts(generic.ListView):
    model = models.Post
    template_name = 'Posts/user_post_list.html'

    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related('Posts').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.Posts.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user
        return context

class PostDetail(SelectRelatedMixin, generic.DetailView):
    model = models.Post
    select_related = ('user', 'group')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))

class CreatePost(LoginRequiredMixin,SelectRelatedMixin,generic.CreateView):

    fields = ('message','group')
    model = models.Post

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class DeletePost(LoginRequiredMixin,SelectRelatedMixin,generic.DeleteView):

    model = models.Post
    select_related = ('user','group')
    success_url = reverse_lazy('Posts:all')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id = self.request.user.id)

    def delete(self,*args,**kwargs):
        messages.success(self.request,'Post Deleted')
        return super().delete(*args,**kwargs)

##############################

class CreateComment(LoginRequiredMixin, generic.CreateView):
    form_class= CommentForm
    model = models.Comment
    success_url = reverse_lazy('Groups:all')

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        post_id = self.kwargs['pk']
        post = models.Post.objects.get(pk=post_id)  
        self.object.post = post
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        print('form invalid')
        print(form.errors.values())
        return render(form, 'Posts/comment_form.html', {'form':form})

#Maybe Later?
    # def get_form(self, form_class=None):
    #     form = super(CreateComment, self).get_form(form_class)
    #     post_id = self.kwargs['pk']
    #     post = models.Post.objects.get(pk=post_id)       
    #     return CommentForm(initial={'post':post})
        

