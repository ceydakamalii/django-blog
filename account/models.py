from django.db import models
from django.contrib.auth.models import AbstractUser
## AbstractUser djangonun user modelini kullanır üzerine eklemeler yapar.
# Create your models here.

class CustomUserModel(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/', blank=True, null= True)


    class Meta:
        db_table='User'
        verbose_name='Kullanıcı'
        verbose_name_plural='Kullanıcılar'
    
    def __str__(self):
        return self.username

