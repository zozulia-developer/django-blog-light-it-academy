from rest_framework import viewsets, generics, mixins
from rest_framework.generics import GenericAPIView

from api.serializer import PostSerializer, CategorySerializer
from posts.models import Post, Category


class PostViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CategoryViewSet(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
