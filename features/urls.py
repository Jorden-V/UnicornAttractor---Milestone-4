from django.conf.urls import url, include
from .views import view_features, feature_detail, add_or_edit_feature, delete_feature, view_completed_features, delete_feature_comment, edit_feature_comments

urlpatterns = [
    url(r'^$', view_features, name='view_features'),
    url(r'^(?P<pk>\d+)/$', feature_detail, name='feature_detail'),
    url(r'^new/$', add_or_edit_feature, name='new_feature'),
    url(r'^(?P<pk>\d+)/edit/$', add_or_edit_feature, name="edit_feature"),
    url(r'^(?P<pk>\d+)/delete/$', delete_feature, name="delete_feature"),
    url(r'^completed_features$', view_completed_features, name='view_completed_features'),
    url(r'^(?P<pk>\d+)/delete/comment$', delete_feature_comment, name="delete_feature_comment"),
    url(r'^(?P<pk>\d+)/edit_feature_comments/$', edit_feature_comments, name="edit_feature_comments"),
]
