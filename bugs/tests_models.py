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
        
    def test_can_create_a_bug_with_a_name_and_desc(self):
        user = User.objects.get(username="test")
        bug = Bug(name="Create a Test", desc=True, author_id=user.id)
        bug.save()
        self.assertEqual(bug.name, "Create a Test")
        self.assertTrue(bug.desc)
        
    def test_name_str(self):
        test_name = Bug(name="A test bug")
        self.assertEqual(str(test_name), "A test bug")
        
class TestBugCommentModel(TestCase):
    
    def test_description_str(self):
        test_description = BugComment(description="A test description")
        self.assertEqual(str(test_description), "A test description")
    