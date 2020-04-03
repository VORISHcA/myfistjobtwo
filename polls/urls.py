from django.conf.urls import url, include
from . import views, addmanydoc
from django.conf import settings

app_name = 'polls'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/add-review/$', views.create_review, name='add-review'),
    url(r'^(?P<pk>[0-9]+)/add/$', addmanydoc.create_new_doctor, name='add'),
    # url(r'^(?P<pk>[0-9]+)/successfully_review/$', views.successfully_review(), name='successfully_review'),
]

