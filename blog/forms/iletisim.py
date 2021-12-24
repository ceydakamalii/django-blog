from django import forms
from blog.models import IletisimModel

##class IletisimForm(forms.Form):
    ##email = forms.EmailField(max_length=100, label='E-mail')
    ##isim_soyisim = forms.CharField(max_length=100, label= 'İsim-Soyisim')
    ##mesaj = forms.CharField(label='Mesajınız', widget=forms.Textarea)

class IletisimForm(forms.ModelForm):
    class Meta:
        model = IletisimModel
        fields = ('isim_soyisim', 'email', 'mesaj')