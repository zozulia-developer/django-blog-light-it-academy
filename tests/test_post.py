import pytest

from pytest_django.fixtures import db

from unittest import mock

from posts.models import Post
from posts.views import index, PostCreateView
from tags.models import Tag, TaggedItem


@pytest.fixture
def post(db):
    post = Post.objects.create(
        title='Title',
        content='Content',
        status=Post.STATUS_PUBLISHED
    )

    tag1 = Tag.objects.create(name='tag 1')
    tag2 = Tag.objects.create(name='tag 2')

    TaggedItem.objects.create(tag=tag1, content_object=post)
    TaggedItem.objects.create(tag=tag2, content_object=post)

    return post


@pytest.mark.django_db
def test_tags_list(post):
    post = Post(title='Title', content='content')

    with mock.patch('posts.models.Post.get_tags_list', return_value=['tag']):
        assert post.get_tags_list() == ['tag']
    # assert post.get_tags_list() == ['tag 2', 'tag 1']


@pytest.mark.django_db
def test_success(post, client):
    resp = client.get('/', follow=True)

    assert resp.status_code == 200\



@pytest.mark.django_db
def test_success_rf(rf, settings):
    request = rf.get('/')

    settings.LOGGING = {}

    response = PostCreateView.as_view()(request)

    assert response.status_code == 200
