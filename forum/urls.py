from django.conf.urls import url, include
from .views import view_posts, post_detail, upvote_post, add_or_edit_post, delete_post, delete_post_comment, edit_post_comments

urlpatterns = [
    url(r'^$', view_posts, name='view_posts'),
    url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),
    url(r'^upvote(?P<pk>\d+)/$', upvote_post, name='upvote_post'),
    url(r'^new/$', add_or_edit_post, name='new_post'),
    url(r'^(?P<pk>\d+)/edit/$', add_or_edit_post, name="edit_post"),
    url(r'^(?P<pk>\d+)/delete/$', delete_post, name="delete_post"),
    url(r'^(?P<pk>\d+)/delete/comment$', delete_post_comment, name="delete_post_comment"),
    url(r'^(?P<pk>\d+)/edit_post_comments/$', edit_post_comments, name="edit_post_comments"),
]
