from celery import shared_task
from django.db.models import Count

from posts.models import Post


@shared_task
def report():
    rep = Post.objects.values('status').aggregate(count=Count('status'))
    return rep


# celery -A blog worker -l INFO - start workers
# celery -A blog beat -l INFO -S django - start celery beat

# celery -A blog worker -B -l INFO - start workers and beat

