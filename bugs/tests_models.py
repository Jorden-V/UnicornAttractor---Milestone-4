from django.test import TestCase, Client
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Bug, BugComment


class TestBugModel(TestCase):

    def setUp(self):
        user = User.objects.create_user(username="test", password="testing")
        self.client.login(username="test", password="testing")
        bug = Bug.objects.create(
            name="test",
            description="testing",
            author_id=user.id)

    def test_desc_defaults_to_False(self):
        user = User.objects.get(username="test")
        bug = Bug(name="Create a Test", author_id=user.id)
        bug.save()
        self.assertEqual(bug.name, "Create a Test")
        self.assertFalse(bug.descriptio)

    def test_can_create_a_bug_with_a_name_and_desc(self):
        user = User.objects.get(username="test")
        bug = Bug(name="Create a Test", description=True, author_id=user.id)
        bug.save()
        self.assertEqual(bug.name, "Create a Test")
        self.assertTrue(bug.description)

    def test_name_str(self):
        test_name = Bug(name="A test bug")
        self.assertEqual(str(test_name), "A test bug")


class TestBugCommentModel(TestCase):

    def test_comment_str(self):
        test_comment = BugComment(comment="A test description")
        self.assertEqual(str(test_comment), "A test description")
