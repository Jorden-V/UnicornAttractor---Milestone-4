from django.conf.urls import url
from .views import graphs

urlpatterns = [
    url(r'^$', graphs, name="graphs"),
]