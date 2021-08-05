from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from django.core.cache import caches, cache

from django.utils.translation import gettext as _

from .models import Post
from .forms import PostForm, LoginForm


class PostListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Post
    template_name = 'post/index.html'
    context_object_name = 'posts'

    login_url = '/login/'
    permission_required = ['can_view_posts']

    def get_queryset(self):
        print(self.request.user)
        print(self.request.user.is_authenticated)
        # return Post.objects.prefetch_related(
        #     'post_categories__category'
        # )
        return Post.objects.published()


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/details.html'
    context_object_name = 'post'


class PostCreateView(CreateView):
    # model = Post
    template_name = 'post/add_post.html'
    form_class = PostForm
    # context_object_name = 'post'
    # fields = ['title', 'content']


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


@login_required(login_url='/login/')
@cache_page(60, cache='db_cache')
def index(request):
    db_cache = caches['db_cache']
    posts = db_cache.get('posts_list', [])
    if not posts:
        posts = Post.objects.all()
        db_cache.set('posts_list', list(posts), 240)
        print('!!!cached')

    posts_title = _('Posts')

    context = {
        'posts': posts,
        'title': posts_title
    }
    # request.session['user_id'] = 111
    # request.session['user_data'] = {
    #     'posts': 32
    # }
    # del request.session['user_id']
    #
    # request.session['user_data']['posts'] = 22
    # request.session.modified = True
    #
    # request.session.set_expiry(0)  # время жизни сессии
    # request.session.flush()  # удалить текущую сессию
    #
    # from django.contrib.auth.models import User
    #
    # user = User.objects.create_user('username', 'email@email.com', 'password')
    # user.set_password('new_password')
    # user.save()

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
    form = PostForm(initial={'title': post.title, 'content': post.content, 'status': post.status})
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post.title = request.POST['title']
            post.content = request.POST['content']
            post.save()
            return redirect('posts:index')
    context = {'post': post, 'form': form}
    return render(request, 'post/edit_post.html', context)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(
                                username=form.cleaned_data['username'],
                                password=form.cleaned_data['password']
            )
            if user.is_active:
                login(request, user)
                return redirect('/posts')
        return render(request, 'post/login.html', {'form': form})
    else:
        form = LoginForm()

    return render(request, 'post/login.html', {'form': form})


def logout_view(request):
    logout(request)

    return redirect('/login/')


def register_view(request):
    User.objects.get(username='admin').check_password('admin')
