# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from .models import Choice, Question
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'lists/index.html'
    context_object_name = 'latest_question_list'
    # context_object_name = 'question'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        )


class DetailView(generic.DetailView):
    model = Question
    template_name = 'lists/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'lists/results.html'


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'lists/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'lists/results.html', {'question': question})
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'lists/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.

        return HttpResponseRedirect(reverse('lists:results',
                                            args=(question.id, )))
        # return HttpResponseRedirect(reverse('lists:index'))


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    print(latest_question_list)
    print('I am here')
    context = {'question': latest_question_list}
    return render(request, 'lists/index.html', context)


def index_temp(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('lists/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
