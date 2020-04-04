from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
import datetime
<<<<<<< HEAD
from django.contrib.auth.models import User, Group


class Items(models.Model):
    name_item = models.CharField(max_length=100, verbose_name='Название Предмета')
    image_item = models.CharField(max_length=100, verbose_name='Ссылка на изображение')
    description_item = models.CharField(max_length=400, verbose_name='Описание Предмета')

    class Meta:
        verbose_name = 'Название'
        verbose_name_plural = 'Название'

    def __str__(self):
        return self.name_item


class Runes(models.Model):
    name_rune = models.CharField(max_length=100, verbose_name='Название Руны')
    image_rune = models.CharField(max_length=100, verbose_name='Ссылка на изображение')
    description_rune = models.CharField(max_length=400, verbose_name='Описание Руны')

    class Meta:
        verbose_name = 'Название'
        verbose_name_plural = 'Название'

    def __str__(self):
        return self.name_rune


class Champions(models.Model):
    name_champion = models.CharField(max_length=100, verbose_name='Название Чемпиона')
    image_champion = models.CharField(max_length=100, verbose_name='Ссылка на изображение')
    description_champion = models.CharField(max_length=400, verbose_name='Описание Чемпиона')

    class Meta:
        verbose_name = 'Название'
        verbose_name_plural = 'Название'

    def __str__(self):
        return self.name_champion


class News(models.Model):
    name_news = models.CharField(max_length=100, verbose_name='Название Новости')
    pub_date = models.DateTimeField('date published')
    image_news = models.CharField(max_length=100, verbose_name='Ссылка на изображение')
    description_news = models.CharField(max_length=400, verbose_name='Описание Новости')

    class Meta:
        verbose_name = 'Название'
        verbose_name_plural = 'Название'

    def __str__(self):
        return self.name_news


class InNews(models.Model):
    section = models.ForeignKey(News, default="", on_delete=models.CASCADE, verbose_name='Новость')
    name_news = models.CharField(max_length=100, verbose_name='Название Новости')
    image_news = models.CharField(max_length=100, verbose_name='Ссылка на изображение')
    all_description_news = models.CharField(max_length=400, verbose_name='Полное Новости')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новость'

    def __str__(self):
        return self.name_news


class Post(models.Model):
    title = models.CharField(max_length=300, unique=True)
    content = models.TextField()


class Section(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Раздел'

    def __str__(self):
        return self.name


class Topic(models.Model):
    section = models.ForeignKey(Section, default="",  on_delete=models.CASCADE, verbose_name='Раздел')
    pub_date = models.DateTimeField('date published')
    review_text = models.CharField(max_length=1000, verbose_name='Исходный текст')
    edit_review_text = models.CharField(max_length=1000, verbose_name='Отредактированный текст')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, verbose_name='Пользователь')
    ip_user = models.CharField(max_length=100, blank=True, verbose_name='ip address')

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Тема'

    def __str__(self):
        return '%s %s' % (self.section.name, self.user.username)


class BadWords(models.Model):
    word = models.CharField(max_length=100, verbose_name='Матерные слова')

    class Meta:
        verbose_name = 'Матерное слово'
        verbose_name_plural = 'Матерные слова'

    def __str__(self):
        return self.word


class NoBadWords(models.Model):
    word = models.CharField(max_length=100, verbose_name='Исключения')

    class Meta:
        verbose_name = 'Исключение'
        verbose_name_plural = 'Исключения'

    def __str__(self):
        return self.word
=======

@python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'



@python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text



>>>>>>> parent of 06a8e76... Day 1
