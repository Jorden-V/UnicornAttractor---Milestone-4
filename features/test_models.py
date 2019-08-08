from django.test import TestCase, Client
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Feature, FeatureComment

class TestFeatureModel(TestCase):
    
    def setUp(self):
        user = User.objects.create_user(username="test", password="testing")
        self.client.login(username="test", password="testing")
        feature = Feature.objects.create(name="test", desc="testing", author_id=user.id)

    def test_desc_defaults_to_False(self):
        user = User.objects.get(username="test")
        feature = Feature(name="Create a Test", author_id=user.id)
        feature.save()
        self.assertEqual(feature.name, "Create a Test")
        self.assertFalse(feature.desc)
        
    def test_can_create_a_feature_with_a_name_and_desc(self):
        user = User.objects.get(username="test")
        feature = Feature(name="Create a Test", desc=True, author_id=user.id)
        feature.save()
        self.assertEqual(feature.name, "Create a Test")
        self.assertTrue(feature.desc)
        
    def test_name_str(self):
        test_name = Feature(name="A test feature")
        self.assertEqual(str(test_name), "A test feature")
        
class TestFeatureCommentModel(TestCase):
    
    def test_description_str(self):
        test_description = FeatureComment(description="A test description")
        self.assertEqual(str(test_description), "A test description")
    