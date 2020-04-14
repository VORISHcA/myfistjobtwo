from django.db import models
#from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
import datetime
from django.contrib.auth.models import User, Group


class SectionNews(models.Model):
    section_news_name = models.CharField(max_length=100, verbose_name='Название раздела новостей')

    class Meta:
        verbose_name = 'Раздел Новости'
        verbose_name_plural = 'Разделы Новости'

    def __str__(self):
        return self.section_news_name


class SectionTopic(models.Model):
    section_topic_name = models.CharField(max_length=100, verbose_name='Название раздела тем')

    class Meta:
        verbose_name = 'Раздел Темы'
        verbose_name_plural = 'Разделы Тем'

    def __str__(self):
        return self.section_topic_name


class Runes(models.Model):
    rune_name = models.CharField(max_length=100, verbose_name='Название руны')
    rune_description = models.CharField(max_length=10000, verbose_name='Описание руны')
    rune_cooldown = models.CharField(max_length=10000, verbose_name='Перезарядка руны')
    rune_image = models.CharField(max_length=200, verbose_name='Изображение руны')

    class Meta:
        verbose_name = 'Руна'
        verbose_name_plural = 'Руны'

    def __str__(self):
        return self.rune_name


class Items(models.Model):
    item_name = models.CharField(max_length=100, verbose_name='Название предмета')
    item_description = models.CharField(max_length=10000, verbose_name='Описание предмета')
    item_stats = models.CharField(max_length=10000, verbose_name='Характеристики предмета')
    item_cooldown = models.CharField(max_length=10000, verbose_name='Перезарядка предмета')
    item_image = models.CharField(max_length=200, verbose_name='Изображение предмета')

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return self.item_name


class Ability(models.Model):
    ability_name = models.CharField(max_length=100, verbose_name='Название способности')
    ability_cooldown = models.CharField(max_length=100, verbose_name='Перезарядка способности')
    ability_damage = models.CharField(max_length=100, verbose_name='Урон способности')
    ability_description = models.CharField(max_length=10000, verbose_name='Описание способности')

    class Meta:
        verbose_name = 'Способность'
        verbose_name_plural = 'Способности'

    def __str__(self):
        return self.ability_name


class Champions(models.Model):
    champion_name = models.CharField(max_length=100, verbose_name='Название Чемпиона')
    rune_description = models.CharField(max_length=10000, verbose_name='Описание Чемпиона')
    rune_image = models.CharField(max_length=200, verbose_name='Изображение Чемпиона')
    champion_hp = models.CharField(max_length=100, verbose_name='Здоровье')
    champion_mp = models.CharField(max_length=100, verbose_name='Мана')
    champion_speed = models.CharField(max_length=100, verbose_name='Скорость')
    champion_attack_speed = models.CharField(max_length=100, verbose_name='Скорость атаки')
    champion_armor = models.CharField(max_length=100, verbose_name='Броня')
    champion_resist = models.CharField(max_length=100, verbose_name='Сопротивление магии')
    champion_damage = models.CharField(max_length=100, verbose_name='Урон')
    champion_ability = models.ManyToManyField(Ability, verbose_name='Специальности')

    class Meta:
        verbose_name = 'Чемпион'
        verbose_name_plural = 'Чемпионы'

    def __str__(self):
        return self.champion_name


class Post(models.Model):
    title = models.CharField(max_length=300, unique=True)
    content = models.TextField()


class News(models.Model):
    news_name = models.CharField(max_length=100, verbose_name='Название новости')
    news_section = models.ForeignKey(SectionNews, default="",  on_delete=models.CASCADE, verbose_name='Раздел')
    pub_date = models.DateTimeField('date published')
    news_text = models.CharField(max_length=1000, verbose_name='Исходный текст')
    edit_news_text = models.CharField(max_length=1000, verbose_name='Отредактированный текст')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, verbose_name='Пользователь')
    ip_user = models.CharField(max_length=100, blank=True, verbose_name='ip address')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новость'

    def __str__(self):
        return '%s %s' % (self.news_section.section_news_name, self.user.username)


class Topics(models.Model):
    topic_name = models.CharField(max_length=100, verbose_name='Название Темы')
    topic_section = models.ForeignKey(SectionTopic, default="",  on_delete=models.CASCADE, verbose_name='Раздел')
    pub_date = models.DateTimeField('date published')
    topic_text = models.CharField(max_length=1000, verbose_name='Исходный текст')
    edit_topic_text = models.CharField(max_length=1000, verbose_name='Отредактированный текст')
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, verbose_name='Пользователь')
    ip_user = models.CharField(max_length=100, blank=True, verbose_name='ip address')

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return '%s %s' % (self.topic_section.section_topic_name, self.user.username)


class Comments(models.Model):
    comment_text = models.CharField(max_length=10000, verbose_name='Текст комментария')
    comment_for_topic = models.ForeignKey(Topics, on_delete=models.CASCADE, blank=True, verbose_name='Тема')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


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
