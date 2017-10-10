# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hellp,world. You're at the polls index.")
# Create your views here.
