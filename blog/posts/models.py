from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    # keywords = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return self.title
