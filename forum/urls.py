from django.conf.urls import url, include
from .views import view_posts, post_detail, upvote_post

urlpatterns = [
    url(r'^$', view_posts, name='view_posts'),
    url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),
    url(r'^upvote(?P<pk>\d+)/$', upvote_post, name='upvote_post'),
    ]