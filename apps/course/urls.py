from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^addnew$', views.addnew),
    url(r'^confirm/(?P<id>\d+)$', views.confirm_page),
    url(r'^remove/(?P<id>\d+)$', views.remove)
]
