from django.test import TestCase
from .forms import CreateBugForm, BugCommentForm



class TestBugForm(TestCase):

    def test_can_create_a_bug_with_name_and_description(self):
        form = CreateBugForm({'name': 'Tests', 'desc': "create a test"})
        self.assertTrue(form.is_valid())

    def test_cannot_create_a_bug_without_required_values(self):
        form = CreateBugForm({'name': 'Test'})
        self.assertFalse(form.is_valid())

    def test_correct_message_for_missing_name(self):
        form = CreateBugForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [u'This field is required.'])

    def test_correct_message_for_missing_desc(self):
        form = CreateBugForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['description'], [u'This field is required.'])


class TestBugCommentForm(TestCase):

    def test_can_create_a_comment_with_required_values(self):
        form = BugCommentForm({'comment': "comment"})
        self.assertTrue(form.is_valid())

    def test_cannot_post_blank_comment(self):
        form = BugCommentForm({'comment': ''})
        self.assertFalse(form.is_valid())
