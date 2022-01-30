from django import forms
from django.contrib.auth import get_user_model
from Posts import models


User = get_user_model()

class PostForm(forms.ModelForm):
    class Meta:
        fields = ("message", "group")
        model = models.Post

        widgets = {
            'title': forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }
    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields["group"].queryset = (
                models.Group.objects.filter(
                pk__in=user.groups.values_list("Groups__pk")
                )
            )

class CommentForm(forms.ModelForm):

    class Meta:
        fields = ('message','post')
        model = models.Comment

        widgets = {
            'message': forms.Textarea(attrs={'class':"editable medium-editor-textarea"}),
            'post': forms.HiddenInput(),
        } 
    
    def __str__(self):
        return f"{self.message} by {self.user}"

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
