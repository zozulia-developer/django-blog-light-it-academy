from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
from .models import Post
from .forms import PostForm


def index(request):
    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'post/index.html', context=context)


def add_post(request):
    # context = {
    #     'post': Post.objects.get()
    # }
    if request == 'GET':
        return render(request, 'post/add_post.html', context={})
    if request == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            p = Post(title=form.cleaned_data['title'], content='')
            p.save()
        else:
            return render(request, 'add_post.html', context={'form': form})
