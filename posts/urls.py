from django.urls import path

from . import views


app_name = 'posts'

urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='details'),
    path('add_post/', views.PostCreateView.as_view(), name='add_post'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post')
]
