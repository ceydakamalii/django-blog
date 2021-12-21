from django.db import models

class IletisimModel(models.Model):
    email = models.EmailField(max_length=250, blank=False, null=False)
    isim_soyisim= models.CharField(max_length=400)
    mesaj= models.TextField()
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='Iletisim'
        verbose_name='Iletisim'
        verbose_name_plural='Iletisim'
    
    def __str__(self):
        return self.email