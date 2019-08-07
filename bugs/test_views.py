from django.test import TestCase, Client
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Bug, BugComment
from django.shortcuts import get_object_or_404

class TestViews(TestCase):
    
    def setUp(self):
        user = User.objects.create_user(username="test", password="testing")
        self.client.login(username="test", password="testing")
        bug = Bug.objects.create(name="test", desc="testing", author=user.id)
    
    def test_get_bugs_page(self):
        page = self.client.get("/view_bugs/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugs.html")

    def test_get_bug_details_page(self):
        page = self.client.get("/bugs/{0}/".format(self.bug.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bug_details.html")

    def test_get_add_bug_page(self):
        page = self.client.get("/view_bugs/new/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "create_bug.html")
        