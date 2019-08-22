from django.test import TestCase, Client
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Feature, FeatureComment
from django.shortcuts import get_object_or_404


class TestViews(TestCase):

    def setUp(self):
        user = User.objects.create_user(username="test", password="testing")
        self.client.login(username="test", password="testing")
        feature = Feature.objects.create(
            name="test", desc="testing", author_id=user.id)

    def test_get_feature_page(self):
        page = self.client.get("/features/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "features.html")

    def test_get_completed_feature_page(self):
        page = self.client.get("/features/completed_features")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "completed_features.html")

    def test_get_feature_details_page(self):
        user = User.objects.get(username="test")
        feature = Feature(
            name="Test title",
            desc="Test description",
            author_id=user.id)
        feature.save()
        response = self.client.get('/features/{}'.format(feature.id))
        self.assertEqual(response.status_code, 301)

    def test_get_add_feature_page(self):
        page = self.client.get("/features/new/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "create_feature.html")

    def test_get_edit_feature_page(self):
        user = User.objects.get(username="test")
        feature = Feature(
            name="Create a Test",
            desc="description",
            author_id=user.id)
        feature.save()

        page = self.client.get("/features/{0}/edit/".format(feature.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "create_feature.html")

    def test_get_edit_page_for_feature_that_does_not_exist(self):
        page = self.client.get("/features/100/edit/")
        self.assertEqual(page.status_code, 404)
