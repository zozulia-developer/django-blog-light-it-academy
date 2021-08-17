from django.urls import path, include

from rest_framework import routers

from api.views import PostViewSet, CategoryViewSet

router = routers.DefaultRouter()
# router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)
# router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:pk>/', PostViewSet.as_view(), name='posts'),
    # path('categories/', CategoryViewSet.as_view(), name='category'),
    path('api-auth/',
         include('rest_framework.urls', namespace='rest_framework'))
]
