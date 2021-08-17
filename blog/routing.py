from django.urls import path
from .consumers import WSConsumer, CommentConsumer

ws_urlpatterns = [
    path('ws/some_url/', WSConsumer.as_asgi()),
    path('ws/posts/<int:pk>/comments/', CommentConsumer.as_asgi())
]
