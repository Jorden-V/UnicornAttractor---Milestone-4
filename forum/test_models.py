from django.test import TestCase, Client
from django.contrib import auth
from django.contrib.auth.models import User
from .models import ForumPost, ForumComment


class TestForumPostModel(TestCase):

    def setUp(self):
        user = User.objects.create_user(username="test", password="testing")
        self.client.login(username="test", password="testing")
        post = ForumPost.objects.create(
            name="test", description="testing", author_id=user.id)

    def test_desc_defaults_to_False(self):
        user = User.objects.get(username="test")
        post = ForumPost(name="Create a Test", author_id=user.id)
        post.save()
        self.assertEqual(post.name, "Create a Test")
        self.assertFalse(post.description)

    def test_can_create_a_post_with_a_name_and_desc(self):
        user = User.objects.get(username="test")
        post = ForumPost(name="Create a Test", description=True, author_id=user.id)
        post.save()
        self.assertEqual(post.name, "Create a Test")
        self.assertTrue(post.description)

    def test_name_str(self):
        test_name = ForumPost(name="A test post")
        self.assertEqual(str(test_name), "A test post")


class TestForumCommentModel(TestCase):

    def test_comment_str(self):
        test_comment = ForumComment(comment="A test comment")
        self.assertEqual(str(test_comment), "A test comment")
