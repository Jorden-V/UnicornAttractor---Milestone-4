from django.conf.urls import url, include
from .views import view_bugs

urlpatterns = [
    url(r'^$', view_bugs, name='view_bugs'),
    url(r'^(?P<pk>\d+)/$', view_bugs, name='view_bugs'),
    ]