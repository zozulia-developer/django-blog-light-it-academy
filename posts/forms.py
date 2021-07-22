from django import forms
from django.forms import ValidationError

from posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'status']
    # title = forms.CharField(
    #     label='Title',
    #     min_length=2,
    #     # max_length=100,
    # )
    # content = forms.CharField(
    #     widget=forms.Textarea,
    #     max_length=1000
    # )
    #

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise ValidationError('validation error!')
        return title
