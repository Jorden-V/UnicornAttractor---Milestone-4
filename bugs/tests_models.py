from django.test import TestCase, Client
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Bug, BugComment

class TestBugModel(TestCase):
    
    def setUp(self):
        user = User.objects.create_user(username="test", password="testing")
        self.client.login(username="test", password="testing")
        bug = Bug.objects.create(name="test", desc="testing", author_id=user.id)

    def test_desc_defaults_to_False(self):
        user = User.objects.get(username="test")
        bug = Bug(name="Create a Test", author_id=user.id)
        bug.save()
        self.assertEqual(bug.name, "Create a Test")
        self.assertFalse(bug.desc)