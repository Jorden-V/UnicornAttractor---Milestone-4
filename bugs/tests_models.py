from django.test import TestCase
from .forms import CreateBugForm, BugCommentForm

# Create your tests here.
class TestBugForm(TestCase):
    
    def test_can_create_a_bug_with_name_and_description(self):
        form = CreateBugForm({'name': 'Tests', 'desc': "create a test"})
        self.assertTrue(form.is_valid())
        
    def test_cannot_create_a_bug_with_required_values(self):
        form = CreateBugForm({'name': 'Test'})
        self.assertFalse(form.is_valid())
    
    def test_correct_message_for_missing_name(self):
        form = CreateBugForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [u'This field is required.'])
        
    def test_correct_message_for_missing_desc(self):
        form = CreateBugForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['desc'], [u'This field is required.'])