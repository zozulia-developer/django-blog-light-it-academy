from django.test import TestCase, Client

from tags.models import Tag, TaggedItem
from posts.models import Category, Post


class PostTestCase(TestCase):
    category_name = 'test category'

    def setUp(self):
        Category.objects.create(name=self.category_name)
        post = Post.objects.create(
            title='Title',
            content='Content',
            status=Post.STATUS_PUBLISHED
        )
        tag1 = Tag.objects.create(name='tag 1')
        tag2 = Tag.objects.create(name='tag 2')

        TaggedItem.objects.create(tag=tag1, content_object=post)
        TaggedItem.objects.create(tag=tag2, content_object=post)

    def test_get_tags_list(self):
        post = Post.objects.get(title='Title')
        self.assertEqual(post.get_tags_list(), ['tag 2', 'tag 1'])

    def test_published(self):
        post = Post.objects.published()
        self.assertEqual(len(post), 1)

        Post.objects.create(title='Title 2', content='content 2')
        self.assertEqual(len(Post.objects.published()), 1)

    # def tearDown(self):
    #     return super().tearDown()
    #
    # @classmethod
    # def setUpClass(cls):
    #     pass
    #
    # @classmethod
    # def tearDownClass(cls):
    #     pass

    def test_post_list(self):
        category = Category.objects.get(name=self.category_name)
        self.assertEqual(str(category), self.category_name)


class PostListViewCase(TestCase):
    fixtures = ['category.json']

    def setUp(self):
        post = Post.objects.create(
            title='Title',
            content='Content',
            status=Post.STATUS_PUBLISHED
        )
        tag1 = Tag.objects.create(name='tag 1')
        tag2 = Tag.objects.create(name='tag 2')

        TaggedItem.objects.create(tag=tag1, content_object=post)
        TaggedItem.objects.create(tag=tag2, content_object=post)

    def test_success(self):
        c = Client(HTTP_ACCEPT='test')

        resp = c.get('/posts/')
        self.assertEqual(resp.status_code, 200)

    def test_create_post_throw_csrf(self):
        c = Client(enforce_csrf_checks=True)

        resp = c.post('/posts/add_post/',
                      follow=True,
                      data={
                          'title': 'title',
                          'content': 'content'
                        }
                      )
        self.assertEqual(resp.status_code, 403)
