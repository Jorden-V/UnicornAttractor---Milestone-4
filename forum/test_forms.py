from django.test import TestCase
from .forms import ForumPostForm, ForumCommentForm

# Create your tests here.


class TestBugForm(TestCase):

    def test_can_create_a_post_with_name_and_description(self):
        form = ForumPostForm({'name': 'Tests', 'desc': "create a test"})
        self.assertTrue(form.is_valid())

    def test_cannot_create_a_post_without_required_values(self):
        form = ForumPostForm({'name': 'Test'})
        self.assertFalse(form.is_valid())

    def test_correct_message_for_missing_name(self):
        form = ForumPostForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [u'This field is required.'])

    def test_correct_message_for_missing_desc(self):
        form = ForumPostForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['desc'], [u'This field is required.'])


class TestForumCommentForm(TestCase):

    def test_can_create_a_comment_with_required_values(self):
        form = ForumCommentForm({'description': "comment"})
        self.assertTrue(form.is_valid())

    def test_cannot_post_blank_comment(self):
        form = ForumCommentForm({'description': ''})
        self.assertFalse(form.is_valid())
