from django.http import HttpResponse, HttpResponseRedirect
# from django.template import RequestContext,loader
from django.urls import reverse
from .models import News, InNews, Section, Items, Runes, Post, Topic, Champions
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.http import Http404
from django.views import generic
from django.utils import timezone
from .forms import PostForm, GetForm
import re


def index(request):
    if request.user.is_superuser:
        latest_review_list = Topic.objects.select_related()
        context = {'latest_review_list': latest_review_list}
        return render(request, 'polls/index.html', context)
    else:
        return render_to_response('polls/sorry.html')

