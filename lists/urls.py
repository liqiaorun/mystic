# -*- coding:utf-8 -*-
from django.conf.urls import url

from . import views

app_name = 'lists'
urlpatterns = [
    # ex: /lists/
    url(r'^$', views.index, name='index'),
    # ex: /lists/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /lists/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /lists/5/vote
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote')
]
