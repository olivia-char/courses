from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^addCourse$', views.addCourse),
    url(r'^remove/(?P<id>\d+$)', views.remove),
    url(r'^delete$', views.delete),
]