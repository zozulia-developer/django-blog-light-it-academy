from django import forms


class PostForm(forms.Form):
    title = forms.CharField(
        label='Title',
        min_length=3,
        max_length=100
    )
    content = forms.CharField(
        widget=forms.Textarea,
        max_length=1000
    )
