# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from lists.models import Question


def index(request):
    return HttpResponse("Hellp,world. You're at the polls index.")
# Create your views here.


def index_temp(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('lists/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
