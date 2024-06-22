from django.db import models

__all__ = ['Food']
class Food(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name')
    price = models.FloatField(verbose_name='Price')
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(upload_to='images/food/')
    isAvailable = models.BooleanField(default=True, name='is_available', verbose_name='Is Available')

    def __str__(self):
        return self.name

