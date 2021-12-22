from enum import unique
from django.db import models
from autoslug import AutoSlugField
from blog.models import KategoriModel
from account.models import CustomUserModel
from ckeditor.fields import RichTextField
from blog.abstract_models import DateAbstractModel

class YazilarModel(DateAbstractModel): 

    resim=models.ImageField(upload_to='yazi_resimleri')
    baslik = models.CharField(max_length=50)
    icerik = RichTextField()
    slug= AutoSlugField(populate_from='baslik', unique=True)
    kategoriler= models.ManyToManyField(KategoriModel, related_name='yazi')
    ## related_name='yazi' ile ters ilişki kurup kategorideki tüm yazıları görebiliyoruz.
    yazar= models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name='yazilar')
    ## on_delete=models.CASCADE burada yazar silinirse yazarın tüm yazılarını siliyoruz.

    class Meta:
        db_table = 'Yazi'
        verbose_name_plural ='Yazilar'
        verbose_name = 'Yazi'
    
    def __str__(self):
        return self.baslik

