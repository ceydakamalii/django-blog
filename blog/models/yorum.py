from django.db import models
from account.models import CustomUserModel
from blog.models import YazilarModel

class YorumModel(models.Model):
    yazan = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name='yorum')
    yazi = models.ForeignKey(YazilarModel, on_delete=models.CASCADE, related_name='yorumlar')
    yorum = models.TextField()
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)
    duzenleme_tarihi=models.DateTimeField(auto_now=True)


    class Meta:
        db_table='Yorum'
        verbose_name='Yorum'
        verbose_name_plural='Yorumlar'
    
    def __str__(self):
        return self.yazan.username

    