from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Post
from .forms import PostForm


class PostListView(ListView):
    model = Post
    template_name = 'post/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.prefetch_related(
            'post_categories',
            'post_categories__category'
        )


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/details.html'
    context_object_name = 'post'


class PostCreateView(CreateView):
    model = Post
    template_name = 'post/add_post.html'
    context_object_name = 'post'
    fields = ['title', 'content']


class MyView(View):
    def get(self, request, *args, **kwargs):
        form = PostForm()
        return render(request, 'post/add_post.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST)
        if form.is_valid():
            p = Post(
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content']
            )
            p.save()
            return redirect('posts:index')
        return render(request, 'post/add_post.html', context={'form': form})


def index(request):
    context = {
        'posts': Post.objects.all(),
    }

    return render(request, 'post/index.html', context)


def post_details(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = PostForm()
    context = {'post': post, 'form': form}
    return render(request, 'post/details.html', context)


def add_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            p = Post(
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content']
            )
            p.save()
            return redirect('posts:index')
    return render(request, 'post/add_post.html', context={'form': form})


def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = PostForm(initial={'title': post.title, 'content': post.content})
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post.title = request.POST['title']
            post.content = request.POST['content']
            post.save()
            return redirect('posts:index')
    context = {'post': post, 'form': form}
    return render(request, 'post/edit_post.html', context)
