from django import forms

from Posts import models


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
