from django.conf.urls import url, include
from .views import view_bugs, bug_detail, upvote_bug

urlpatterns = [
    url(r'^$', view_bugs, name='view_bugs'),
    url(r'^(?P<pk>\d+)/$', bug_detail, name='bug_detail'),
    url(r'^upvote(?P<pk>\d+)/$', upvote_bug, name='upvote_bug'),
    ]