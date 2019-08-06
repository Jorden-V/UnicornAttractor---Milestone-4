from django.conf.urls import url, include
from .views import view_posts

urlpatterns = [
    url(r'^$', view_posts, name='view_posts'),
    ]