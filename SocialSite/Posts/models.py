from django.db import models
from django.urls import reverse
from django.conf import settings
import misaka
from Groups.models import Group, GroupMember
from django.contrib.auth import get_user_model

# Create your models here.
#Get current user session
User = get_user_model()

class Post(models.Model):
    """
    Class: Post model
    Attributes:
    User: Foreign key associated with User model that is initialized by get_user_model()
    Date Created: Date time field with current time as input
    Message: User text field description
    Message HTML: markdown safe text description of Message attribute
    Group: Foreign key associated with Group model, imported from Groups app
    """
    user = models.ForeignKey(User,related_name='Posts', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, related_name='Posts',null=True,blank=True, on_delete = models.CASCADE)

    #return stringified msg
    def __str__(self):
        return self.message

    def save(self,*args,**kwargs):
        #misaka here allows messages with html, etc. to display correctly
        self.message_html = misaka.html(self.message)
        super().save(*args,**kwargs)    

    #This will create the url link for the post. 
    def get_absolute_url(self):
        return reverse("Posts:single", kwargs={"username":self.user.username,
                                                "pk": self.pk})


    
    class Meta:
        #descending order of created at value
        ordering = ['-created_at']
        #every message is linked to a unique user
        unique_together = ['user', 'message']

class Comment(models.Model):
    """
    Class: Comment model
    Attributes:
    Post" Foreign key associated with Post PK
    User: Foreign key associated with User model that is initialized by get_user_model()
    Date Created: Date time field with current time as input
    Message: User text field description
    Message HTML: markdown safe text description of Message attribute
    Group: Foreign key associated with Group model, imported from Groups app
    """
    post = models.ForeignKey(Post, related_name='comments', null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='commenter', null=True, blank=True, on_delete=models.CASCADE)
    message_html = models.TextField(editable=False, null=True, blank=True)
    message = models.TextField()
    create_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message    

    def save(self,*args,**kwargs):
        #misaka here allows messages with html, etc. to display correctly
        self.message_html = misaka.html(self.message)
        super().save(*args,**kwargs)    

    def get_absolute_url(self):
        return reverse('post_list', kwargs={"username":self.user.username,
                                                "pk": self.pk})

    class Meta:
        #descending order of created at value
        ordering = ['-create_date']



