from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^$', views.index),
    url(r'push/(?P<target>\w+)$', views.push, name='push'),
]
