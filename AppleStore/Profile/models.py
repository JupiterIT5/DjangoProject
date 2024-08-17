from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user_lastname = models.CharField(max_length=255, verbose_name='Фамилия')
    user_name = models.CharField(max_length=255, verbose_name='Имя')
    user_surname = models.CharField(max_length=255, verbose_name='Отчество')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    photo = models.ImageField(upload_to='images/users/%Y/%m/%d', blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
    
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'