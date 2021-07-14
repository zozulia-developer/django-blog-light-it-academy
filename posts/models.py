from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        null=True,
        default=None,
        related_name='posts'
    )
    categories = models.ManyToManyField(
        'Category',
        through='PostCategory'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class PostCategory(models.Model):
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE
    )
    is_main = models.BooleanField(default=False)
