from django.test import TestCase
from django.contrib.auth.models import User
from .models import Blog


class BlogModelTest(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(username='testuser1', password='testpassword1')
        self.user2 = User.objects.create_user(username='testuser2', password='testpassword2')
        self.blog1 = Blog.objects.create(
            title='Go',
            content='Learning go.',
            author=self.user1
        )
        self.blog2 = Blog.objects.create(
            title='Frontend',
            content='Learning frontend.',
            author=self.user2
        )

    def test_title(self):
        obj1 = Blog.objects.get(id=self.blog1.id)
        obj2 = Blog.objects.get(id=self.blog2.id)

        self.assertEqual(obj1.title, 'Go')
        self.assertEqual(obj2.title, 'Frontend')

        self.assertIsNotNone(obj1.created_at)

    def test_content(self):
        obj1 = Blog.objects.get(id=self.blog1.id)
        obj2 = Blog.objects.get(id=self.blog2.id)

        self.assertEqual(obj1.content, 'Learning go.')
        self.assertEqual(obj2.content, 'Learning frontend.')

    def test_data(self):
        obj1 = Blog.objects.get(id=self.blog1.id)
        obj2 = Blog.objects.get(id=self.blog2.id)

        self.assertIsNotNone(obj1.created_at)
        self.assertIsNotNone(obj2.created_at)

