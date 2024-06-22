from django.db import models

__all__ = ['User']

class User(models.Model):
    username = models.CharField(max_length=50, verbose_name='Username')
    password = models.CharField(max_length=50, verbose_name='Password')
    email = models.EmailField(max_length=50, verbose_name='Email')
    phone = models.CharField(max_length=50, verbose_name='Phone')
    address = models.CharField(max_length=50 , verbose_name='Address')
    userImage = models.ImageField(upload_to='images/profile/')
    isActive = models.BooleanField(default=True, name='is_active', verbose_name='Is Active')
    isDeleted = models.BooleanField(default=False, name='is_deleted', verbose_name='Is Deleted')

    def __str__(self):
        return self.username