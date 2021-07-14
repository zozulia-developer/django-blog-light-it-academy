from django.urls import path

from . import views


app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.post_details, name='details'),
    path('add_post/', views.add_post, name='add_post'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post')
]
