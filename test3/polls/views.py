
from django.http import HttpResponse, HttpResponseRedirect
# from django.template import RequestContext,loader
from django.urls import reverse

from .models import News, Topics, SectionNews, SectionTopic, Champions, User, Group, Items, Runes, Ability, BadWords, NoBadWords
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render_to_response
from django.http import Http404
from django.views import generic
from django.utils import timezone
from .forms import PostForm, GetForm
import re


def check_news(request):
    latest_news_list = News.objects.select_related()
    context = {'latest_news_list': latest_news_list}
    return render(request, 'polls/news.html', context)


def check_topic(request):
    latest_topic_list = Topics.objects.select_related()
    context = {'latest_topic_list': latest_topic_list}
    return render(request, 'polls/topics.html', context)


def check_item(request):
    latest_item_list = Items.objects.select_related()
    context = {'latest_topic_list': latest_item_list}
    return render(request, 'polls/items.html', context)


def check_champion(request):
    latest_champions_list = Champions.objects.select_related()
    context = {'latest_topic_list': latest_champions_list}
    return render(request, 'polls/champions.html', context)


def check_rune(request):
    latest_rune_list = Runes.objects.select_related()
    context = {'latest_topic_list': latest_rune_list}
    return render(request, 'polls/rune.html', context)


'''
def check_ability_champion(request):
    latest_topic_list = News.objects.select_related()
    context = {'latest_topic_list': latest_topic_list}
    return render(request, 'polls/topics.html', context)
'''


def create_topic(request, pk):

    info_topic = Topics.objects.get(id=pk)
    context = {'info_topic': info_topic}
    if request.method == 'POST':
        if request.POST.get('content'):
            post = Topics()
            post.pub_date = timezone.now()
            post.topic_text = request.POST.get('content')
            post.user = request.user
            post.topic_id = pk
            post.edit_topic_text = create_new_edit_text(post.topic_text)
            post.save()
            # return render(request, 'polls/add-topic.html')
            return render(request, 'polls/successfully_topic.html', context)
    else:
        return render(request, 'polls/add-topic.html', context)


def create_news(request, pk):
    if request.user.is_superuser:
        info_topic = News.objects.get(id=pk)
        context = {'info_news': info_topic}
        if request.method == 'POST':
            if request.POST.get('content'):
                post = News()
                post.pub_date = timezone.now()
                post.news_text = request.POST.get('content')
                post.user = request.user
                post.news_id = pk
                post.edit_topic_text = create_new_edit_text(post.news_text)
                post.save()
                # return render(request, 'polls/add-topic.html')
                return render(request, 'polls/successfully_news.html', context)
        else:
            return render(request, 'polls/add-news.html', context)
    else:
        return render_to_response('polls/sorry.html')


def create_new_edit_text(string):
    all_bad = BadWords.objects.all()
    all_no_bad = NoBadWords.objects.all()
    mas_all_bad = []
    mas_all_no_bad = []
    for i in all_bad:
        mas_all_bad.append(i.word)
    for i in all_no_bad:
        mas_all_no_bad.append(i.word)

    symbol = ['!', '?', '.', ',', ':']
    j = 0
    if re.search(r'[A-ZÀ-ß]{6}', string):
        string = string.lower()
        for i in range(len(string) - 1):
            if string[i].isupper and string[i + 1].isupper:
                string = string.lower()
        t = True
        for i in range(len(string)):
            if t:
                t = False
                if string[i] == ' ':
                    string = string[:i] + ' ' + string[i + 1].upper() + string[i + 2:]
                else:
                    string = string[:i] + string[i].upper() + string[i + 1:]
            if string[i] in ['!', '.', '?']:
                t = True
    while j < len(string) - 1:
        if string[j] == string[j + 1] and string[j] in symbol:
            string = string[:j] + string[j + 1:]
        else:
            j = j + 1

    i = 0

    while i < len(string) - 1:
        if string[i] in symbol:
            if string[i - 1] == ' ':
                string = string[:i - 1] + string[i:]
            if string[i + 1] != ' ':
                string = string[:i + 1] + ' ' + string[i + 1:]
        i = i + 1
    new_string = string.split(' ')
    create_string = ''
    for i in range(len(new_string)):
        local_new_string = new_string[i].lower()
        local_new_string = re.sub('[^à-ÿ]', '', local_new_string)
        if not local_new_string in mas_all_no_bad:
            for j in range(len(mas_all_bad)):
                if mas_all_bad[j] in local_new_string:
                    new_string[i] = "<span class ='highlight'>" + new_string[i] + "</span>"
        create_string = create_string + new_string[i] + ' '

    return create_string


def topic_detail(request, pk):
    post = get_object_or_404(Topics, pk=pk)
    return render(request, 'polls/topic_detail.html', {'post': post})


def news_detail(request, pk):
    post = get_object_or_404(News, pk=pk)
    return render(request, 'polls/news_detail.html', {'post': post})

