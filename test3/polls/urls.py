from django.conf.urls import url, include
from . import views
from django.conf import settings

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/create_topic/$', views.create_topic, name='create_topic'),
    url(r'^(?P<pk>[0-9]+)/create_news/$', views.create_news, name='create_news'),
    url(r'^news/', views.check_news, name='check_news'),
    url(r'^items/<int:pk>/', views.check_item, name='check_item'),
    url(r'^champions/<int:pk>/', views.check_champion, name='check_champion'),
    url(r'^rune/<int:pk>/', views.check_rune, name='check_rune'),
    url(r'^topics/', views.check_topic, name='check_topic'),
    url(r'^news/', views.check_news, name='check_news'),
    url(r'^topics/', views.check_topic, name='check_topic'),
    # url(r'^(?P<pk>[0-9]+)/successfully_review/$', views.successfully_review(), name='successfully_review'),
]

