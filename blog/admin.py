from django.contrib import admin
from blog.models import KategoriModel, YazilarModel, YorumModel, IletisimModel

# Register your models here.
admin.site.register(KategoriModel)

@admin.register(YazilarModel)
class YazilarAdmin(admin.ModelAdmin):
    search_fields=('baslik','icerik')
    list_display=(
        'baslik', 'olusturulma_tarihi', 'duzenleme_tarihi'
    )
#admin.site.register(YazilarModel, YazilarAdmin)

@admin.register(YorumModel)
class YorumAdmin(admin.ModelAdmin):
    search_fields =('yazan_username',)
    list_display=('yazan', 'olusturulma_tarihi', 'duzenleme_tarihi')

#admin.site.register(YorumModel, YorumAdmin)

@admin.register(IletisimModel)
class IletisimAdmin(admin.ModelAdmin):
    
    list_display=('isim_soyisim', 'email', 'olusturulma_tarihi')

#admin.site.register(IletisimModel, IletisimAdmin)

