from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Tag(models.Model):
    name = models.CharField(max_length=100)


class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


'''
from tags.models import Tag, Post
from posts.models import  Post
from django.contrib.contenttypes.models import ContentType
ct_post = ContentType.objects.get(app_label='posts', model='post')
tag_1 = Tag.objects.get(name='random tag')
ti = TaggedItem(tag=tag_1, content_type=ct_post, object_id=1)
post = Post.objects.get(id=1)
ti = TaggedItem(tag=tag_1, content_object=post)
post_tags = new_post.tags.all()
for p in post_tags:
    print(p.tag.name)
'''
