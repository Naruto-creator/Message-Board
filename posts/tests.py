from django.test import TestCase
from django.urls import reverse

from .models import Post


class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(post="just")

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.post}'
        self.assertEqual(expected_object_name, "just")


class HomePageViewTest(TestCase):

    def setUp(self):
        Post.objects.create(post="text fot home page")

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
























































