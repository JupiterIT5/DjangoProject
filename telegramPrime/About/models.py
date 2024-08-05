from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

MAX_LENGTH = 255


class Post(models.Model):
    title = models.CharField(max_length=MAX_LENGTH, verbose_name='Название поста')
    description = models.TextField(max_length=MAX_LENGTH, verbose_name='Описание поста')
    tag = models.OneToOneField('Tag', on_delete=models.PROTECT, verbose_name='Тег')
    image = models.ImageField(upload_to='images/%Y/%m%d', default='images/no_photo.png', null=True, blank=True, verbose_name='Обложка поста')
    post = CKEditor5Field(config_name='extends', verbose_name="Пост")
    
    def __str__(self):
        return f'{self.pk} || {self.title}'
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        

class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'