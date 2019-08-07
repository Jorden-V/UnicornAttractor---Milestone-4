from django.test import TestCase, Client
from .models import Bug, BugComment
from django.contrib.auth import get_user_model

User = get_user_model()

class TestViews(TestCase):
    
    def setUp(self):
        
        """
        Set up temporary users and a bug for testing purposes. 
        Code by Marcin Mrugacz: 
        https://github.com/Migacz85/django_app/blob/master/bugs/tests.py
        """
        
        self.user = User.objects.create(
            username='admin',
            password='asdfg',
            is_active=True,
            is_staff=True,
            is_superuser=True
        )
        self.user.set_password("asdfg")
        self.user.save()

        self.user = User.objects.create(
            username='John',
            password='asdfg',
            is_active=True,
            is_staff=True,
            is_superuser=False
        )
        self.user.set_password("asdfg")
        self.user.save()
        
        self.client = Client()
        self.bug = Bug.objects.create(
            name='test',
            desc='this is a test',
            author=self.user
        )
        self.bug.save()
    
    def test_get_bugs_page(self):
        page = self.client.get("/view_bugs/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugs.html")
        
    def test_get_bug_details_page(self):
        page = self.client.get("/bugs/{0}/".format(self.bug.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bug_details.html")

    def test_add_bug_page(self):
        page = self.client.get("/view_bugs/new/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "create_bug.html")
        