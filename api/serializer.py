from rest_framework import serializers

from posts.models import Post, Category


class PostSerializer(serializers.HyperlinkedModelSerializer):
    status = serializers.CharField(max_length=100)
    title = serializers.CharField(max_length=100)
    content = serializers.CharField(max_length=100)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Post
        fields = ['status', 'title', 'content', 'created_at']


class CategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
