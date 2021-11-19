from django.db import models


class Currency(models.Model):
    user = models.CharField('Пользователь', max_length=150)
    cryptocurrency = models.CharField('Криптовалюта', max_length=150)
    cryptocurrency_symbol = models.CharField('символ', max_length=150)
    price = models.IntegerField('цена', blank=True, null=True)


    def __str__(self):
        return self.user
    
    class Meta:
        verbose_name = 'Клиенты'
        verbose_name_plural = 'Клиент'