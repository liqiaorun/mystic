# -*- coding:utf-8 -*-
from django.conf.urls import url

from . import views

app_name = 'lists'
urlpatterns = [
    # ex: /lists/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /lists/5/
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # the 'name' value as called by the {% url %} template tag
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /lists/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(),
        name='results'),
    # ex: /lists/5/vote
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
