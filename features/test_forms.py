from django.test import TestCase
from .forms import CreateFeatureForm, FeatureCommentForm

# Create your tests here.


class TestFeatureForm(TestCase):

    def test_can_create_a_feature_with_name_and_description(self):
        form = CreateFeatureForm({'name': 'Tests', 'description': "create a test"})
        self.assertTrue(form.is_valid())

    def test_cannot_create_a_feature_without_required_values(self):
        form = CreateFeatureForm({'name': 'Test'})
        self.assertFalse(form.is_valid())

    def test_correct_message_for_missing_name(self):
        form = CreateFeatureForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [u'This field is required.'])

    def test_correct_message_for_missing_desc(self):
        form = CreateFeatureForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['description'], [u'This field is required.'])


class TestFeatureCommentForm(TestCase):

    def test_can_create_a_comment_with_required_values(self):
        form = FeatureCommentForm({'comment': "comment"})
        self.assertTrue(form.is_valid())

    def test_cannot_post_blank_comment(self):
        form = FeatureCommentForm({'comment': ''})
        self.assertFalse(form.is_valid())
