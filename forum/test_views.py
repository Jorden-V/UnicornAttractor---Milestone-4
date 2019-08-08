from django.test import TestCase, Client
from django.contrib import auth
from django.contrib.auth.models import User
from .models import ForumPost, ForumComment
from django.shortcuts import get_object_or_404

class TestViews(TestCase):
    
    def setUp(self):
        user = User.objects.create_user(username="test", password="testing")
        self.client.login(username="test", password="testing")
        post = ForumPost.objects.create(name="test", desc="testing", author_id=user.id)
    
    def test_get_forum_page(self):
        page = self.client.get("/view_posts/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "forum.html")

    def test_get_forum_details_page(self):
        user = User.objects.get(username="test")
        post = ForumPost(name="Test title", desc="Test description", author_id=user.id)
        post.save()
        response = self.client.get('/view_posts/{}'.format(post.id))
        self.assertEqual(response.status_code, 301)

    def test_get_add_post_page(self):
        page = self.client.get("/view_posts/new/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "create_post.html")
        
    def test_get_edit_bug_page(self):
        user = User.objects.get(username="test")
        post = ForumPost (name="Create a Test", desc="description", author_id=user.id)
        post.save()

        page = self.client.get("/view_posts/{0}/edit/".format(post.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "create_post.html")
        
    def test_get_edit_page_for_post_that_does_not_exist(self):
        page = self.client.get("/view_posts/100/edit/")
        self.assertEqual(page.status_code, 404)


