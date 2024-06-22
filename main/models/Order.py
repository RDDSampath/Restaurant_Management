from django.db import models
from .User import User
from .Food import Food

__all__ = ['Order']
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='Quantity')
    total = models.FloatField(verbose_name='Total')
    orderDate = models.DateTimeField(auto_now_add=True, verbose_name='Order Date')
    isDelivered = models.BooleanField(default=False, name='is_delivered', verbose_name='Is Delivered')

    def getTotal(self):
        return self.food.price * self.quantity

    def __str__(self):
        return self.user.username + ' - ' + self.food.name