from django.shortcuts import get_object_or_404, render, redirect
from blog.models import YazilarModel
from blog.forms import YorumEkleModelForm
from django.views import View
from django.contrib import messages

class DetayView(View):
    http_method_names=['get','post']
    yorum_ekle_formu = YorumEkleModelForm

    def get(self, request, slug):
        yazi = get_object_or_404(YazilarModel, slug=slug)
        yorumlar = yazi.yorumlar.all()
        return render(request, 'pages/detay.html',context={
            'yazi': yazi,
            'yorumlar': yorumlar,
            'yorum_ekle_form': self.yorum_ekle_formu()
        })
    def post(self, request, slug):
        yazi = get_object_or_404(YazilarModel, slug=slug)
        yorum_ekle_form = self.yorum_ekle_formu(data=request.POST)
        if yorum_ekle_form.is_valid():
            yorum=yorum_ekle_form.save(commit=False)
            yorum.yazan=request.user
            yorum.yazi=yazi
            yorum.save()
            messages.success(request, 'Yorum başarılı bir şekilde eklendi')
        return redirect('detay', slug=slug)



