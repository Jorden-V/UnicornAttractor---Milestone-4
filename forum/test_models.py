from django.test import TestCase, Client
from django.contrib import auth
from django.contrib.auth.models import User
from .models import ForumPost, ForumComment


class TestForumPostModel(TestCase):

    def setUp(self):
        user = User.objects.create_user(username="test", password="testing")
        self.client.login(username="test", password="testing")
        post = ForumPost.objects.create(
            name="test", desc="testing", author_id=user.id)

    def test_desc_defaults_to_False(self):
        user = User.objects.get(username="test")
        post = ForumPost(name="Create a Test", author_id=user.id)
        post.save()
        self.assertEqual(post.name, "Create a Test")
        self.assertFalse(post.desc)

    def test_can_create_a_post_with_a_name_and_desc(self):
        user = User.objects.get(username="test")
        post = ForumPost(name="Create a Test", desc=True, author_id=user.id)
        post.save()
        self.assertEqual(post.name, "Create a Test")
        self.assertTrue(post.desc)

    def test_name_str(self):
        test_name = ForumPost(name="A test post")
        self.assertEqual(str(test_name), "A test post")


class TestForumCommentModel(TestCase):

    def test_description_str(self):
        test_description = ForumComment(description="A test description")
        self.assertEqual(str(test_description), "A test description")
