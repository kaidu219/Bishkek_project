from django.db import models
import uuid
from datetime import datetime
from multiselectfield import MultiSelectField


# Create your models here.
class News(models.Model):

    category = (
        ('','Культура'),
        ('','Интернет'),
        ('','Наука и технологии'),
        ('','Некрологи'),
        ('','Общество'),
        ('','Политика'),
        ('','Преступность и право'),
        ('','Проишествия'),
        ('','Рейтинги'),
        ('','Религия'),
        ('','Дни рождения'),
        ('','Спорт'),
        ('','Экономика'),
    )


    id = models.UUIDField(default=uuid.uuid4, null=False, blank=False, editable=False, primary_key=True)
    title_news = models.CharField(max_length=255, null=True)
    text_news = models.CharField(max_length=500, null=False)
    time_news = models.DateTimeField(auto_now_add=True)
    correspondent_fname = models.CharField(max_length=255, null=True)
    category_news = MultiSelectField(choices=category, max_length=255, null=True)

    def __str__(self) -> str:
        return self.title_news
    
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'



class About_city(models.Model):
    id = models.UUIDField(default=uuid.uuid4, null=False, blank=False, editable=False, primary_key=True)
    bloger_name = models.CharField(max_length=255, null=False)
    url_channel = models.URLField(max_length=255, blank=True)
    title_article = models.CharField(max_length=255, null=True)
    text_article = models.CharField(max_length=500, null=False)
    url_video = models.URLField(max_length=255, blank=True)

    def __str__(self) -> str:
        return self.bloger_name + ': ' + self.title_article
    
    class Meta:
        verbose_name = 'About_city'
        verbose_name_plural = 'About_city'
