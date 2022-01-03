from django.db import models


class UserRequest(models.Model):
    name = models.CharField(max_length=300, verbose_name='Имя')
    phone = models.CharField(max_length=16, verbose_name='Телефон')
    email = models.EmailField(max_length=300, verbose_name='Электронная почта')
    processed = models.BooleanField(default=False, verbose_name='Обработано')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка пользователя'
        verbose_name_plural = 'Заявки пользователей'
