from django import forms


class PostForm(forms.Form):
    title = forms.CharField(min_length=5)
    content = forms.CharField(max_length=100)
