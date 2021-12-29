from django import forms
from blog.models import IletisimModel
from django.core.mail import send_mail
##class IletisimForm(forms.Form):
    ##email = forms.EmailField(max_length=100, label='E-mail')
    ##isim_soyisim = forms.CharField(max_length=100, label= 'İsim-Soyisim')
    ##mesaj = forms.CharField(label='Mesajınız', widget=forms.Textarea)

class IletisimForm(forms.ModelForm):
    class Meta:
        model = IletisimModel
        fields = ('isim_soyisim', 'email', 'mesaj')
    
    def send_email(self, mesaj):
        send_mail(
            subject='İletişim Formundan Yeni Mesaj Var !',
            message=mesaj,
            from_email=None,
            recipient_list=['ceydakamali3@gmail.com'], ##kime gönderilcek
            fail_silently=False ##send_emailin hatalarını yakalamak için false yapıyoruz.
        )