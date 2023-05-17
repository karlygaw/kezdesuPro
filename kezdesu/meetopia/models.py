from django.db import models
from django.urls import reverse
import uuid


class MeetingSphere(models.Model):
    code = models.CharField(max_length=36, default=uuid.uuid4, unique=False, null=True, verbose_name="Код")
    slug = models.SlugField(max_length=255,  db_index=True, verbose_name="URL")
    name = models.CharField(max_length=255, verbose_name="Название")
    date = models.DateTimeField(blank=True, null=True, verbose_name="Время")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время обновления")
    message = models.TextField(blank=True, verbose_name="Сообщение")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="Категории")
    cuisine = models.ForeignKey('Cuisine', on_delete=models.PROTECT, null=True, verbose_name="Вид кухни")
    place = models.ForeignKey('Place', on_delete=models.PROTECT, null=True, verbose_name="Места")

    class Meta:
        verbose_name = "Встречи"
        verbose_name_plural = "Встречи"



    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         self.code = str(uuid.uuid4())[:8].replace('-', '').upper()
    #     super(MeetingSphere, self).save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('join_meeting', kwargs={'code': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['id']

class Cuisine(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    def str(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cuisine', kwargs={'cui_id': self.pk})

class Place(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def str(self):
        return self.name

    def get_absolute_url(self):
        return reverse('place', kwargs={'place_id': self.pk})
    
