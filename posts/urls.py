from django.urls import path
from django.views.decorators.cache import cache_page

from . import views


app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/',
         cache_page(60, cache='db_cache')(views.PostDetailView.as_view()),
         name='details'),
    path('add_post/', views.PostCreateView.as_view(), name='add_post'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post')
]
